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