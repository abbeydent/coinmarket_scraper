from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

for one_file_name in glob.glob("html_files/*.html"):
	print("parsing " + one_file_name)
	scrapping_time = os.path.splitext(os.path.basename(one_file_name))[0].replace("coinmarketcap","")
	f = open(one_file_name, "r")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
	currencies_table = soup.find("table", {"id": "currencies-all"})
	currencies_tbody = currencies_table.find('tbody')
	currency_rows = currencies_tbody.find_all("tr")
	for r in currency_rows:
		currency_short_name = r.find("td", {"class": "currency-name"}).find("span",{"class":"currency-symbol"}).find("a").text
		currency_name = r.find("td", {"class": "currency-name"}).find("a",{"class":"currency-name-container"}).text
		currency_market_cap = r.find("td", {"class": "market-cap"})['data-sort']
		currency_price = r.find("a",{"class": "price"}).text
		currency_volume = r.find("a",{"class": "volume"}).text
		currency_supply = r.find("td", {"class": "circulating-supply"})['data-sort']
		currency_change = r.find("td", {"class": "percent-change"})['data-sort']
		print(currency_short_name)


# url = 'https://coinmarketcap.com/all/views/all/'

# for root, dirs, files in os.walk("html_files"):
# 	for file in files:
# 		if file.endswith('.html'):
# 			print("parsing" + file)
# 			scrapping_time = os.path.splitext(os.path.basename(file))[0].replace("coinmarketcap", "")
# 			f = open(file, "r")
# 			soup = BeautifulSoup(f.read(), 'html.parser')
# 			f.close()
# 			currencies_table = soup.find("table", {"id": "currencies-all"})
# 			currencies_tbody = currencies_table.find("tbody")
# 			currency_rows = currencies_tbody.find_all("tr")
# 			for r in currency_rows: 
# 				currency_short_name = r.find("td", {"class": "currency-name"}).find("span", {"class": "currency-symbol"}).find("a").text
# 				currency_name = r.find("td", {"class": "currency-name"}).find("a", {"class": "currency-name-container"}).text
# 				currency_market_cap = r.find("td", {"class": "market-cap"})['data-sort']
# 				currency_prince = r.find("a", {"class": "price"}).text
# 				currency_supply = r.find("td", {"class": "circulating-supply"})['data-sort']
# 				currency_volume = r.find("a", {"class": "volume"}).text
# 				currency_change = r.find("td", {"class": "percent-change"}, {"data-timespan": "24h"})['data-sort']

