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

#############################################################################################################
import requests
from bs4 import BeautifulSoup
import time

# req = 'тренажерные%20залы'
# num = 2
# page = requests.get(f'https://moscow.flamp.ru/search/тренажерные%20залы?page={num}')
# soup = BeautifulSoup(page.text, 'html5lib')
# links = soup.find_all(class_='card__link')
# href_list = []


def one_page_parse(links_list):
    for l in range(len(links_list)):
        lnk = links_list[l].get('href')
        # href_list.append(lnk)
        with open('fit_links', 'a') as fl:
            fl.writelines(lnk + '\n')


def main_parse(pages_qty):
    """
    :param pages_qty: количество страниц для парсинга
    :return:
    """
    q = 1
    while q <= pages_qty:
        page = requests.get(f'https://moscow.flamp.ru/search/тренажерные%20залы?page={q}')
        soup = BeautifulSoup(page.text, 'html5lib')
        links = soup.find_all(class_='card__link')
        one_page_parse(links)
        q += 1
        time.sleep(1)


main_parse(81)

# list_href = []
# while num < 3:
#     page = requests.get(f'https://moscow.flamp.ru/search/{req}?page={num}')
#     soup2 = BeautifulSoup(page.text, 'html5lib')
#     links = soup2.find_all('a', class_='card__link')
#     for i in range(len(links)):
#         list_href.append(links[i].get('href'))
#     i += 1
# print(list_href)


import requests
from bs4 import BeautifulSoup
import re

req = requests.get('https://moscow.flamp.ru/firm/zebra_fitness_sportivno_ozdorovitelnyjj_kompleks-4504127908530212')
soup = BeautifulSoup(req.text, 'html5lib')
feed = soup.find_all(class_='t-rich-text__p')
# text = feed.contents[0]
# text1 = str(re.findall(r'\S+', text))
print(feed)
# with open('feed', 'a') as f:
#     f.write(text)



