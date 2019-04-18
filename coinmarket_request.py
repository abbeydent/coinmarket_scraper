import urllib.request
import os
import time
import datetime
from bs4 import BeautifulSoup

if not os.path.exists("html_files"):
	os.mkdir("html_files")

url = 'https://coinmarketcap.com/all/views/all/'

for i in range(1):
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
	f = open("html_files/coinmarketcap" + current_time_stamp +".html", "wb")
	response = urllib.request.urlopen('https://coinmarketcap.com/all/views/all/')
	html = response.read()
	#print(html)
	f.write(html)
	f.close()
	time.sleep(10)





