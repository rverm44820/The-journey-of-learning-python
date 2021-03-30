import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
#1 html
url ='https://www.marketwatch.com/investing/stock/aapl?mod=over_search'

page = requests.get(url)
#print(page)

soup = BeautifulSoup(page.text,'lxml')
#print(soup)
#2price of stock
price = soup.find('h3',class_ ='intraday__price').text
print(price)


#3closing price of stock
close = soup.find_all('span',class_ = 'primary')[2].text

print('close',close)


#4 52 week range
nested = soup.find('mw-rangebar',class_ = 'element element--range range--yearly')
#print(nested)

lower = nested.find_all('span',class_ = 'primary')[0].text
print('lower',lower)

upper = nested.find_all('span',class_ = 'primary')[1].text
print('upper',upper)
#fif2wkl = soup.find_all('span',class_ = 'primary')[4].text
#print(fif2wkl)

#fif2wkh = soup.find_all('span',class_ = 'primary')[5].text
#print(fif2wkh)

#5 analyst rating
anarat = soup.find('li', class_='analyst__option active').text
print(anarat)


