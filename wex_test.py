import requests
import lxml
from bs4 import BeautifulSoup
import re


price = requests.get('https://wex.nz/api/3/ticker/btc_usd')
x = (price.json().get('btc_usd').get('last'))
rub = requests.get('https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json')
print(rub.json())
price_rub = x * 63.2
print(x, price_rub)
response = requests.get('https://localbitcoins.net/ru/buy-bitcoins-online/rub/')
text = response.text

soup = BeautifulSoup(text, 'lxml')
a = soup.find('td', class_='column-price')
lbc1 = (a.contents)[0].split('RUB')
lbc2 = re.findall(r'\S+', str(lbc1[0]))
lbc3 = lbc2[0].split(',')
str = int(float(lbc3[0] + lbc3[1]))
# lbc4 = float(lbc3[0])

spread = price_rub - str
print(spread)

###########################
import requests
import lxml
from bs4 import BeautifulSoup
import re

req = 'тренажерный%20зал'
# num = 1
# page = requests.get(f'https://moscow.flamp.ru/search/{req}?page={num}')
# info = page.text

# price = requests.get('https://wex.nz/api/3/ticker/btc_usd')
# x = (price.json().get('btc_usd').get('last'))
# rub = requests.get('https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json')
# print(rub.json())
# price_rub = x * 63.2
# print(x, price_rub)
# response = requests.get('https://localbitcoins.net/ru/buy-bitcoins-online/rub/')
# text = response.text
#
# soup = BeautifulSoup(text, 'html5lib')
# a = soup.find('td', class_='column-price')
# lbc1 = (a.contents)[0].split('RUB')
# lbc2 = re.findall(r'\S+', str(lbc1[0]))
# lbc3 = lbc2[0].split(',')
# str = int(float(lbc3[0] + lbc3[1]))
# # lbc4 = float(lbc3[0])
#
# spread = price_rub - str
num = 1
# soup = BeautifulSoup(info, 'html5lib')
# a = soup.find_all('a', class_='card__link')
list_href = []
while num < 3:
    page = requests.get(f'https://moscow.flamp.ru/search/{req}?page={num}')
    soup2 = BeautifulSoup(page.text, 'html5lib')
    links = soup2.find_all('a', class_='card__link')
    for i in range(len(links)):
        list_href.append(links[i].get('href'))
    i += 1
print(list_href)

