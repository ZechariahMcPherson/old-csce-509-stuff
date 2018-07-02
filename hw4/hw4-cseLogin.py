#Creator: Gregory Zechariah McPherson
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

#sign in information
user = "username"
password = "password"

info = {'name': user, 'pass': password}

#sign in and get response webpage
html = requests.post("https://cse.sc.edu/user/login?destination=node", data= info)

#put webpage into BeautifulSoup object
bsObj = BeautifulSoup(html.text, "html.parser")

#open file for printing
htmlFile = open("hw4-cseLogin.txt", 'w', encoding='utf-8')

#print prettified webpage
htmlFile.write(bsObj.prettify())
