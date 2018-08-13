#!/usr/bin/env python

# To get the HTTP response for various URL combinations
import requests

# To get the final URL if the URL is redirected 
import urllib2

# List of possible appendices you have to add to find out the platform
# and the product listing page containing all the products in that domain

app=['/categories','/products','/collections','/shop',
     '/index.php?route=product/search&search=%20','/catalog',
     'catalog/products','catalog/product_list']

# Function which performs the required task and returns both the platform
# as well as the URL which contains all the products
# Function Input: Domain Name for example, joco.com or shultzilla.com

def func(domn):

    
    '''
      Adding http to the domain name so that it becomes a valid URL,
      it is safe to add http instead of https since some of the old websites
      still run on http, it is ok even if we add http for a website using https
      because it gets redirected to the same domain name with https, my code is
      ablt to handle such redirects.
    '''
    t="http://"+domn

    # Getting the domain name to check in case of a redirect 
    dom=domn[0:domn.find('.')]
    
    try:
        for i in app:
            url=t+i   # URL to be tried

            r = requests.head(url) # Getting the response
            
            print(r.status_code)    # Status code of the response

            
            if r.status_code==200:  # meaning the URL exists
                
                print(url)

                # The final list which is going to be returned
                ans=[]  
                ans.append(url)

                # Checking what platform was used to develop the website based on
                # which appendix caused a valid URL response

                if i=='/categories':
                    ans.append('BigCommerce')

                if i=='/shop' or i=='/products':
                    ans.append('WooCommerce')
                    ans.append('Shopify')

                if i=='/index.php?route=product/search&search=%20':  
                            ans.append('OpenCart')    

                if i=='/collections':
                    ans.append('Shopify')

                if i=='/catalog' or i=='/catlog/products' or i=='catalog/product_list':
                    ans.append('PrestaShop')

                # Printing and returning what is to be returned
                print(ans)
                return ans


            # In case of a Temporary/Primary redirect of the URL which we are trying
            elif r.status_code==302 or r.status_code==301:
                
                try:
                    
                    # To get the final URL
                    resp=urllib2.urlopen(url)
                    # getting the final URL after redirection
                    finalurl=resp.geturl()
                    # printing the final url
                    print('Final URL:') 
                    print(finalurl)

                    # The final list which is going to be returned
                    ans=[]
                    
                    # Checking if the final URL which was obtained
                    # after redirection belongs to the same domain 
                    if dom in finalurl:
                        ans.append(finalurl)

                        
                        # Checking what platform was used to develop the website based on
                        # which appendix caused a valid URL response

                        if i=='/categories':
                            ans.append('BigCommerce')
                            
                        if i=='/shop' or i=='/products':
                            ans.append('WooCommerce')
                            ans.append('Shopify')

                        if i=='/index.php?route=product/search&search=%20':  
                            ans.append('OpenCart')
                            
                        if i=='/collections':
                            ans.append('Shopify')
                            
                        if i=='/catalog' or i=='/catlog/products' or i=='catalog/product_list':
                            ans.append('PrestaShop')

                         # Printing and returning what is to be returned    
                        print(ans)
                        return ans
                    
                    else:
                        # If the URL redirects to apage with a different domain 
                        # name than the one with which we began with
                        return None

                # If the URL redirects to a non-existing page than we continue
                # to check if some other appendix works
                except:
                    continue

        # If None of the appendices work we return None
        return None

    # In case of a bad URL or some other Connection Error
    except requests.ConnectionError:
        print("failed to connect")


# An Example Function call:
# func('shultzilla.com')

# This Function returns a list whose first element is the URL which contains
# all the product URLs of the E-Commerce Website and the
# rest of the elements of the list are the possible platforms that were
# used to build the given E-Commerce Website.

