#!/usr/bin/env python
# /*************************************************************************
#  * 
#  * Ideas2IT Confidential
#  * _____________________
#  * 
#  *  2016 Ideas2IT Technology Services Private Limited.
#  *  All Rights Reserved.
#  * 
#  * NOTICE:  All information contained herein is, and remains
#  * the property of Ideas2IT Technology Services Private Limited and its
#  * suppliers, if any.  The intellectual and technical concepts contained
#  * herein are proprietary to Ideas2IT Technology Services Private Limited
#  * and its suppliers and may be covered by Indian and Foreign Patents,
#  * patents in process, and are protected by trade secret or copyright law.
#  * Dissemination of this information or reproduction of this material
#  * is strictly forbidden unless prior written permission is obtained
#  * from Ideas2IT Technology Services Private Limited.
#  *
# *************************************************************************/

import socket
import signal
import sys
import ideacrawler_pb2
import ideacrawler_pb2_grpc
import grpc

import time
from Queue import Queue
from threading import Thread

## imports for clientcode
import re

class CrawlerRunThread(Thread):
    def __init__(self, ccObj):
        Thread.__init__(self)
        self.ccObj = ccObj

    def run(self):
        self.ccObj.Run()
        
class CrawlerCallback(Thread):
    def __init__(self, domainQueue, callback, ccObj):
        Thread.__init__(self)
        self.domainQueue = domainQueue
        self.callback = callback
        self.ccObj = ccObj

    def run(self):
        while True:
            if self.domainQueue.empty():
                time.sleep(0.05)
            else:
                # Get the work
                PageHTML = self.domainQueue.get()
                self.domainQueue.task_done()
                # print >> sys.stderr, 'PageHTML "%s" ' % PageHTML.url
                if None != self.callback:
                    self.callback(PageHTML, self.ccObj)

class AddPagesThread(Thread):
    def __init__(self, ideaCrawlerStub, subscription, pageRequestQueue, pageResponseQueue):
        Thread.__init__(self)
        self.ideaCrawlerStub = ideaCrawlerStub
        self.subscription = subscription
        self.pageRequestQueue = pageRequestQueue
        self.pageResponseQueue = pageResponseQueue

    def run(self):
        def urlGen():
            while True:
                if self.pageRequestQueue.empty():
                    time.sleep(0.05)
                else:
                    pageUrl, metaStr = self.pageRequestQueue.get()
                    self.pageRequestQueue.task_done()
                    yield ideacrawler_pb2.PageRequest(sub=self.subscription, reqtype=ideacrawler_pb2.GET, url=pageUrl, metaStr=metaStr)

        for response in self.ideaCrawlerStub.AddPages(urlGen()):
            self.pageResponseQueue.put(response)

class ClientCrawler():
    def ctrlc_handler(self, signal, frame):
        print("Sending cancel to server\n")
        self.Stop()
        sys.exit(0)

    def __init__(self, svrHost="", svrPort="2345", seedURL = "", callback = None):
        # domainOpt params
        self.seedURL            = seedURL
        self.minDelay              = 5
        self.maxDelay              = 0
        self.callback           = callback
        self.follow             = True
        self.followUrlRegexp    = ""
        self.callbackUrlRegexp  = ""
        self.callbackXpathMatch = []
        self.callbackXpathRegexp = []
        self.impolite           = False    # set to true to not check robots.txt
        self.unsafeNormalizeURL = False
        self.checkContent       = False
        self.chrome             = False
        self.chromeBinary       = "/usr/bin/chromium-browser"
        self.domLoadTime        = 5
        self.networkIface       = ""
        self.useragent          = "Fetchbot"
        self.maxConcurrentRequests = 5
        self.checkLoginAfterEachPage = False
        
        #login
        self.login    = False
        self.loginUrl = ""
        self.loginPayload = []
        self.loginParseFields = False
        self.loginParseXpath = []
        self.loginSuccessCheck = None

        # operational variables
        self.svrHost           = svrHost
        self.svrPort           = svrPort
        self.pageRequestQueue  = Queue()
        self.ideaCrawlerStub     = None
        self.subscription      = None
        self.pageResponseQueue = Queue()
        self.AddPagesThread    = None
        self.runThread         = None

        signal.signal(signal.SIGINT, self.ctrlc_handler)
    def setServer(self, svrHost, svrPort="2345"):
        self.svrHost = svrHost
        self.svrPort = svrPort

    def setLogin(self, loginUrl, loginPayload={}, loginParseXpath={}, loginSuccessCheck=None):
        self.login = True
        self.loginUrl = loginUrl
        for key in loginPayload:
            self.loginPayload.append(ideacrawler_pb2.KVP(key=key, value=loginPayload[key]))
        if len(loginParseXpath) > 0:
            self.loginParseFields=True
        for key in loginParseXpath:
            self.loginParseXpath.append(ideacrawler_pb2.KVP(key=key, value=loginParseXpath[key]))
        if loginSuccessCheck == None:
            return
        for key in loginSuccessCheck:
            self.loginSuccessCheck = ideacrawler_pb2.KVP(key=key, value=loginSuccessCheck[key])

    def setCallbackXpathMatch(self, mdata):   #mdata is dict {'xpath':'match', 'xpath':'match", ...}
        for key in mdata:
            self.callbackXpathMatch.append(ideacrawler_pb2.KVP(key=key, value=mdata[key]))

    def setCallbackXpathRegexp(self, mdata):
        for key in mdata:
            self.callbackXpathRegexp.append(ideacrawler_pb2.KVP(key=key, value=mdata[key]))

    def PromptForDomain(self):
        DomainOpt = ideacrawler_pb2.DomainOpt(seedUrl=self.seedURL,
                                              minDelay=self.minDelay,
                                              maxDelay=self.maxDelay,
                                              noFollow = not self.follow,
                                              followUrlRegexp=self.followUrlRegexp,
                                              callbackUrlRegexp=self.callbackUrlRegexp,
                                              callbackXpathMatch=self.callbackXpathMatch,
                                              callbackXpathRegexp=self.callbackXpathRegexp,
                                              impolite=self.impolite,
                                              unsafeNormalizeURL=self.unsafeNormalizeURL,
                                              checkContent=self.checkContent,
                                              chrome=self.chrome,
                                              chromeBinary=self.chromeBinary,
                                              domLoadTime=self.domLoadTime,
                                              login=self.login,
                                              loginUrl=self.loginUrl,
                                              loginPayload=self.loginPayload,
                                              loginParseFields=self.loginParseFields,
                                              loginParseXpath=self.loginParseXpath,
                                              loginSuccessCheck=self.loginSuccessCheck,
                                              checkLoginAfterEachPage=self.checkLoginAfterEachPage,
                                              networkIface=self.networkIface,
                                              useragent=self.useragent,
                                              maxConcurrentRequests=self.maxConcurrentRequests
        )
        # print >> sys.stderr, 'Prompt "%s" ' % DomainOpt.seedUrl
        return DomainOpt

    def Start(self):
        self.runThread = CrawlerRunThread(self)
        self.runThread.daemon = True
        self.runThread.start()
        time.sleep(2)

    def IsAlive(self):
        if self.runThread == None:
            return False
        return self.runThread.isAlive()

    def Wait(self):
        signal.pause()
#        self.runThread.join()
    
    def Run(self):
        ts = time.time()

        domainQueue = Queue()
        channel = grpc.insecure_channel(self.svrHost + ':' + self.svrPort)
        self.ideaCrawlerStub = ideacrawler_pb2_grpc.IdeaCrawlerStub(channel)
        responses = self.ideaCrawlerStub.AddDomainAndListen(self.PromptForDomain())
        self.subscription = next(responses).sub

        callbackWorker = CrawlerCallback(domainQueue, self.callback, self)
        # Setting daemon to True will let the main thread exit even though the workers are blocking
        callbackWorker.daemon = True
        callbackWorker.start()

        for response in responses:
            domainQueue.put(response)

        print('Crawling took {} seconds'.format(time.time() - ts))

    def AddPage(self, url, metaStr = ""):
        if self.AddPagesThread == None:
            self.AddPagesThread = AddPagesThread(self.ideaCrawlerStub, self.subscription,
                                            self.pageRequestQueue, self.pageResponseQueue)
            self.AddPagesThread.daemon = True
            self.AddPagesThread.start()
        self.pageRequestQueue.put((url, metaStr))

    def Stop(self):
        self.ideaCrawlerStub.CancelJob(self.subscription)


if __name__ == "__main__":
    def printURL(ph, ccObj):
        print ph.success, ph.httpstatuscode, ph.error, ph.url, ph.metaStr
        if re.compile('coinmarketcap.*\/currencies\/[^\/]+\/$').search(ph.url):
            newurl = ph.url + "historical-data/?start=20130428&end=20170912"
            print "Adding:", newurl
            ccObj.AddPage(newurl)
            
        with open(ph.url.replace('/', '').replace(':', '').replace('?', ''), "wb") as text_file:
            text_file.write(ph.content.encode('UTF-8'))


    z = ClientCrawler("127.0.0.1", "2345", "https://www.irctc.co.in/eticketing/loginHome.jsf", printURL)
    z.set_Follow(False)
#    z = ClientCrawler("127.0.0.1", "2345", "https://www.linkedin.com/in/raja-sankar-7a0ab269/", printURL)
    z.RunJob()
