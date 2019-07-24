from bs4 import BeautifulSoup
import requests
import re
from subprocess import Popen
import subprocess
import os
import time
from selenium import webdriver

url = "http://vrsiddhartha.ac.in/index.php/component/content/category/3"
#url = "http://shanmukhavishnu.in"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)
search="VR17"
results1 = soup.body.find_all(string=re.compile('.*{0}.*'.format(search)), recursive=True)
sto = len(results1)
while True:
	print("Waiting for Results to be Declared")
	results = soup.body.find_all(string=re.compile('.*{0}.*'.format(search)), recursive=True)
	if len(results) > sto: #7 Results with name VR17 already present in the page, if Results arraived the name +VR17 name exists
		subprocess.Popen(['notify-send', "Results Declared"])
		subprocess.Popen(['notify-send', "Opening Results Page"])
		break
	else:
		print("Results not yet declared")
	time.sleep(5)
browser= webdriver.Firefox()
print("opening firefox")
browser.get(url)