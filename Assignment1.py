#!/usr/bin/python

from bs4 import BeautifulSoup 
import lxml.html
import urllib3
import requests
import sys  

if (len(sys.argv) <= 1): 
	print("Not Enough Arguments!") 

else: 
	print("Number Of Arguments Accepted!") 
	url = sys.argv[1] 
	request = requests.get(url)
	data = request.text 
	soup = BeautifulSoup(data, 'lxml')
	current_link = ''
	links = soup.find_all('a')
	for link in links:
		current_link = link.get('href')
		if(current_link.endswith('.pdf')):
			print('PDF: ' + current_link)
		else: 
			pass
