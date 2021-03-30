import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
url ='https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

page = requests.get(url)
#print(page)
soup = BeautifulSoup(page.text,'lxml')
#print(soup.prettify().encode('utf-8'))
product_name=soup.find_all('a', class_ = 'title')
#print(product_name)
price= soup.find_all('h4', class_ ='pull-right price')
#print(price)
reviews = soup.find_all('p', class_ = re.compile('pull'))
#print(reviews)
description= soup.find_all('p',class_ = 'description')
#print(description)
ggg= soup.find('h4',{'class':'pull-right price'}).text
#print(ggg)

product_name_list =[]
for i in product_name:
    name=i.text
    #print(name)
    product_name_list.append(name)
print(product_name_list)

price_list =[]
for i in price:
    price2=i.text
    #print(name)
    price_list.append(price2)
print(price_list)

reviews_list =[]
for i in reviews:
    reviews2=i.text
    #print(name)
    reviews_list.append(reviews2)
print(reviews_list)

descriptions_list =[]
for i in description:
    description2=i.text
    #print(name)
    descriptions_list.append(description2)
print(descriptions_list)

table= pd.DataFrame({'Product Name' :product_name_list, 'Description': descriptions_list,
                     'Price': price_list, 'Reviews': reviews_list})
print(table)


boxes = soup.find_all('div',class_ ='col-sm-4 col-lg-4 col-md-4')[6]
#print(boxes)

aaa=boxes.find('a').text
#print(aaa)

bbb=boxes.find('p',class_ ='description').text
#print(bbb)

box2 = soup.find_all('ul', class_ = 'nav', id = 'side-menu')[0]
print(box2)

ccc=box2.find_all('li')[1]
#print(ccc)

ddd= box2.find_all('li')[1].text
print(ddd)
