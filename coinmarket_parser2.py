from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("parsed_historical_files"):
	os.mkdir("parsed_historical_files")

df = pd.dataframe[]

for one_file_name in glob.glob("historical_html_files/*.html"):
	print("parsing " + one_file_name)
	f = open(one_file_name, "r")
	soup = BeautifulSoup(f.read(), 'html.parser')
	f.close()
	historical_table = soup.find("table")
	tbody = historical_table.find("tbody")
	rows = tbody.find_all("tr")
	for r in rows:
		tds = r.find_all("td")
		date = tds[0].text
		open_price = tds[1].text
		high = tds[2].text
		low = tds[3].text
		close_price = tds[4].text
		volume = tds[5].text
		market_cap = tds[6].text
		# print(tds)
		# print(date)
		# print(open_price)
		# print(high)
		# print(low)
		# print(cose_price)
		# print(volume)
		# print(market_cap)
		df = df.append({
			'date': date,
			'open_price': open_price,
			'high': high,
			'low': low,
			'close_price': close_price,
			'volume': volume,
			'market_cap': market_cap
			}, ignore_index=True)


#print(df)
df.to_csv("parsed_historical_files/coinmarket_historical_dataset")
