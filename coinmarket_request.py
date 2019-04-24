import urllib.request
import os
import time
import datetime
from bs4 import BeautifulSoup
import pandas as pd 

if not os.path.exists("html_files"):
	os.mkdir("html_files")

url = 'https://coinmarketcap.com/all/views/all/'

for i in range(30):
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
	print("requesting " + url + current_time_stamp)
	f = open("html_files/coinmarketcap" + current_time_stamp +".html", "wb")
	response = urllib.request.urlopen('https://coinmarketcap.com/all/views/all/')
	html = response.read()
	#print(html)
	f.write(html)
	f.close()
	time.sleep(21600)

f = open("html_files/coinmarketcap.html", "r")
soup = BeautifulSoup(f.read(), features='lxml')
f.close()
currencies_table = soup.find("table", {"id": "currencies-all"})
currencies_tbody = currencies_table.find("tbody")
currency_rows = currencies_tbody.find_all("tr")
crypto_list = []
crypto_name_list = []
for r in currency_rows:
	currency_short_name = r.find("td", {"class": "currency-name"}).find("span", {"class": "currency-symbol"}).find("a").text
	currency_name = r.find("td", {"class": "currency-name"}).find("a",{"class":"currency-name-container"}).text
	currency_link = r.find("td", {"class": "currency-name"}).find("a", {"class": "currency-name-container"})['href']
	crypto_list.append(currency_link)
	crypto_name_list.append(currency_short_name)
	#print(crypto_list)

if not os.path.exists("historical_html_files"):
	os.mkdir("historical_html_files")

# print(crypto_list[1:5])
# print(crypto_name_list[1:5])

for i in range(500):
	print("requesting " + crypto_name_list[i])
	f = open("historical_html_files/" + crypto_name_list[i]  + ".html", "wb")
	# print("https://coinmarketcap.com" + crypto_list[i]  + "historical-data" + "?start=20130428&end=20190422")
	response = urllib.request.urlopen("https://coinmarketcap.com" + crypto_list[i]  + "historical-data" + "?start=20130428&end=20190422")
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(30)

	 
			







