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

from ver2 import func
import os
import sys
sys.path.insert(0, os.path.expanduser('/media/bhargav/Windows/Users/bharg/Desktop/PipeCandy/ideacrawler.v0.2.0/pyclient'))
import pyclient
import time

#ans=func('tattly.com')


def main():
    def savePage(ph, ccObj):
        print(ph.success, ph.httpstatuscode, ph.error, ph.url, ph.metaStr)
        print(ph.content)
#        with open("out.file", "wb") as text_file:
#            text_file.write(ph.content)

    
    z = pyclient.ClientCrawler("127.0.0.1", "2345")
    z.callback           = savePage
    z.seedURL            = ""
    z.follow             = True
    z.unsafeNormalizeURL = True
    z.impolite           = True
    z.followUrlRegexp    = ""
    z.callbackUrlRegexp  = ""    
    z.minDelay           = 1
    z.maxDelay           = 3

    z.Start()

    z.AddPage('https://shop.landrover.com/uk/catalogsearch/result/index/?q=1%3D%3D1&product_list_limit=all', "100")
#    z.AddPage("http://milindhg.github.io", "42")
#    z.AddPage("https://github.com/search?q=fullname:Mohammad+Badruzzaman+location:Berlin&type=Users", "42")
    while True:
        if z.IsAlive():
            time.sleep(1)
        else:
            break
   

main()
