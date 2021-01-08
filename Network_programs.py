import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup

class Soupbot():
    
    def findPrice(self):
        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        url = 'https://www.amazon.com/dp/B0000Y7KNQ/ref=nav_timeline_asin?_encoding=UTF8&psc=1'

        # Amazon Price Checker

        html = urllib.request.urlopen(url,context=ctx).read()
        soup = BeautifulSoup(html,'html.parser')
        price = soup.find(id = 'priceblock_ourprice').text
        return price
    def findName(self):
        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        url = 'https://www.amazon.com/dp/B0000Y7KNQ/ref=nav_timeline_asin?_encoding=UTF8&psc=1'

        # Amazon Price Checker

        html = urllib.request.urlopen(url,context=ctx).read()
        soup = BeautifulSoup(html,'html.parser')
        productTitle = soup.find(id = 'productTitle').text
        return productTitle.strip()


# Debug 

# title = Soupbot().findName()
# print (title)
    

