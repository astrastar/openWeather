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

