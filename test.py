from bs4 import BeautifulSoup
import os
import glob


# crypto_list =["bitcoin","ethereum","litecoin"]

# for i in crypto_list:
# 	print(i)
# 	print('https://coinmarketcap.com/currencies/' + i + '/historical-data/?start=20130428&end=20190415')

# td_list = ['<td class="text-left">Apr 15, 2019</td>','<td data-format-fiat="" data-format-value="167.897474089">167.90</td>','<td data-format-fiat="" data-format-value="168.818458462">168.82</td>','<td data-format-fiat="" data-format-value="159.555732914">159.56</td>','<td data-format-fiat="" data-format-value="161.574178302">161.57</td>','<td data-format-market-cap="" data-format-value="5672311823.76">5,672,311,824</td>','<td data-format-market-cap="" data-format-value="17074367782.6">17,074,367,783</td>']

# print(td_list[0])
# print(td_list[1])
# print(td_list[2])


f = open("html_files/coinmarketcap.html", "r")

soup = BeautifulSoup(f.read(), 'html.parser')

currencies_table = soup.find("table", {"id": "currencies-all"})
currencies_tbody = currencies_table.find("tbody")
currency_rows = currencies_tbody.find_all("tr")

for r in currency_rows:
	currency_short_name = r.find("td", {"class": "currency-name"}).find("span", {"class": "currency-symbol"}).find("a").text
	currency_name = r.find("td", {"class": "currency-name"}).find("a", {"class": "currency-name-container"}).text

print(currency_name)



#crypto_list = list()



#parser starts here:
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



#scrapper starts here
	from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

#os.chdir("/Users/abbey_dent/Desktop/MachineLearning/coinmarket_cap/")
if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")


df = pd.DataFrame()

for coinmarket_cap in glob.glob("html_files/*.html"):
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

	

## request

for i in range(2):
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
	f = open("html_files/coinmarketcap" + current_time_stamp +".html", "wb")
	response = urllib.request.urlopen('https://coinmarketcap.com/all/views/all/')
	html = response.read()
	#print(html)
	f.write(html)
	f.close()
	time.sleep(10)
