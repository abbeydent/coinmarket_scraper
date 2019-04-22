from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("parsed_historical_files"):
	os.mkdir("parsed_historical_files")

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
		print(open_price)
