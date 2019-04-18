from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

#os.chdir("/Users/abbey_dent/Desktop/MachineLearning/coinmarket_cap/")
if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")


df = pd.DataFrame()

for coinmarketcap in glob.glob("html_files/*.html"):
	print("parsing " + coinmarketcap)
	scrapping_time = os.path.splitext(os.path.basename(coinmarketcap))[0].replace("coinmarketcap","")
	f = open(coinmarketcap, "r")
	soup = BeautifulSoup(f.read(), features="lxml")
	f.close()
	currencies_table = soup.find("table", {"id": "currencies"})
	print(currencies_table)
	#currencies_tbody = soup.findcurrencies_table.find("tbody")
	#currency_rows = currencies_tbody.find_all("tr")
	#for r in currency_rows:
		#currency_short_name = r.find("td", {"class": "currency-name"}).find("span",{"class":"currency-symbol"}).find("a").text
		#currency_name = r.find("td", {"class": "currency-name"}).find("a",{"class":"currency-name-container"}).text
		#currency_market_cap = r.find("td", {"class": "market-cap"})['data-sort']
		#currency_price = r.find("a",{"class": "price"}).text
		#currency_volume = r.find("a",{"class": "volume"}).text
		#currency_supply = r.find("td", {"class": "circulating-supply"})['data-sort']
		#currency_change = r.find("td", {"class": "percent-change"})['data-sort']
		#print(scraping_time)
		#print(currency_short_name)

	

