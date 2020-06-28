'''
Created with Love By Shanmukha Vishnu
Twitter : @iam_shanmukha
blog: www.shanmukhavishnu.in
'''
import tweepy
from bs4 import BeautifulSoup
import requests
import re
from subprocess import Popen
import subprocess
from os import *
import time
from selenium import webdriver

#######################################Twitter########################
consumer_key =environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token =environ['access_token']
access_token_secret =environ['access_token_secret']
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
###################################Twitter Data Ends ################
####################################MAin#############################
url = "http://www.vrsiddhartha.ac.in/examination-archives/"
#url = "http://WWW.shanmukhavishnu.in"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)
search="VR17"
results1 = soup.body.find_all(string=re.compile('.*{0}.*'.format(search)), recursive=True)
#Searching for VR17 and store len(results1) in variable sto. In next step, recusively search for VR17. if Results declared new "VR17" added to site and so len(resulst)> sto.
#Hence opens Examination link
sto = len(results1)
#print(sto)
while True:
	print("Waiting for Results to be Declared")
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')
	search="VR17"
	results = soup.body.find_all(string=re.compile('.*{0}.*'.format(search)), recursive=True)
	#print(len(results)) At the time of annoucing results if any new term of VR17 added to the site, it will reflected here
	if len(results) > sto:
		subprocess.Popen(['notify-send', "Results Declared"])
		subprocess.Popen(['notify-send', "Opening Results Page"])
		api.update_status(status ='Notification on VR17 Arraived\n' + url)
		break
	else:
		print("Results not yet declared")
	time.sleep(5)
browser= webdriver.Firefox()
print("opening firefox")
browser.get(url)
