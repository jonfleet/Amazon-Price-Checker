import requests
from bs4 import BeautifulSoup

path_URL = ''


class Soupbot:
    def __init__(self):
        self.header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
        
    
    def find_price(self,URL):
        self.page = requests.get(URL, headers = self.header)
        self.soup = BeautifulSoup(self.page.content,'html.parser')
        self.soup2 = BeautifulSoup(self.soup.prettify(),'html.parser')
        price = self.soup2.find_all("div", class_= "list-card-heading")
        return print(price)

Soup = Soupbot()
print(Soup.find_price(path_URL))

# header =  {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
# page = requests.get(path_URL,headers = header)
# soup = BeautifulSoup(soup.page.content, 'html.parser')
# print(soup)
# soup2 = BeautifulSoup(soup.prettify(), 'html.parser')
# price = soup.find(id = "priceblock_ourpice")
# print(price)


#--------------------------------

# print(soup.title.string)
# for item in 
# print(soup.find_all('span', id = "priceblock_ourprice")
# for tag in soup.find('span'):
#     print(tag)
# match = soup.find_all("div",class_= "a-section")
# print(match)

# print(soup.find("span",id="priceblock_ourprice"))
# Title 

# print(soup.title)
# print("-------")
# print(soup.title.name)
# print("--------")
# print(soup.title.string)
# print("--------")
# print(soup.title.parent.name)

# Body 

# print(soup.body)
# print("-------")
# print(str(soup.body.name))
# print("-------")
# print(soup.body.string)

# for link in soup.find_all('a'):
#     print(link.get('href'))

# print(soup.get_text())

# title = soup.find(id="productTitle")


# title2 = BeautifulSoup(title,'html.parser')

