from bs4 import BeautifulSoup
import os
import glob

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

url = 'https://coinmarketcap.com/all/views/all/'

f = open("html_files/coinmarketcap.html", "r")
#g = open("coinmarketcap20190416162540.html", "r")


#print(f.read())

soup = BeautifulSoup(f.read(), 'html.parser')
#soup1 = BeautifulSoup(g.read(), 'html.parser')


#print(soup)

#for one_file_name in glob.glob("html")
currencies_table = soup.find("table", {"id": "currencies-all"})
currencies_tbody = currencies_table.find("tbody")
currency_rows = currencies_tbody.find_all("tr")


for r in currency_rows: 
	currency_short_name = r.find("td", {"class": "currency-name"}).find("span", {"class": "currency-symbol"}).find("a").text
	currency_name = r.find("td", {"class": "currency-name"}).find("a", {"class": "currency-name-container"}).text
	currency_market_cap = r.find("td", {"class": "market-cap"})['data-sort']
	currency_prince = r.find("a", {"class": "price"}).text
	currency_supply = r.find("td", {"class": "circulating-supply"})['data-sort']
	currency_volume = r.find("a", {"class": "volume"}).text
	currency_change = r.find("td", {"class": "percent-change"}, {"data-timespan": "24h"})['data-sort']
	# link = r.find("a", {"class": "currency-name-container"}, 'href')
	# 	for l in link:
	# 	historic_table = soup1.find("table", {"class": "table"})
	# 	historic_tbody = historic_table.find("tbody")
	# 	historic_rows = historic_tbody.find_all("tr")
	# 	for r in historic_rows:
			





	#print(currency_short_name)
	print(currency_name)
	#print(currency_change)
	#print(currency_market_cap)






