#Creator: Gregory Zechariah McPherson
from selenium import webdriver as webdriver
from urllib.request import urlopen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common import keys
from bs4 import BeautifulSoup
import os
import time

"""
I spent around seven hours trying to get firefox to work on the lab machines. I never got it to work. Firefox is the only browser I could use selenium on in the lab. So I did the project on my computer and used chrome. A few of my friends had the same issue and did it on their local machines as well.
"""


def create_output_file(name):
    """creates output file"""

    if os.path.isfile(name):
        os.remove(name)
    newFile = open(name,"w+")

    return newFile

def dump_html(page, tag):
    """makes html look nice and puts it into a file"""

    bsObj = BeautifulSoup(page, 'html.parser')
    niceDoc = bsObj.prettify()

    outputFileName = ("output" + tag +".txt")

    file = create_output_file(outputFileName)

    file.write(niceDoc)

    file.close()

def signin (browser, address):
    """signs into yahoo"""

    browser.get(address)

    WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "login-username")))

    btn = browser.find_element_by_id("login-signin")

    username = browser.find_element_by_name("username")
    username.send_keys("gzm@email.sc.edu")

    btn.click()

    #required due to hidden element issues
    time.sleep(3)

    btn = browser.find_element_by_name("signin")

    password = browser.find_element_by_name("passwd")

    password.send_keys("ignorethis")

    btn.click()

def main ():

    #firefox didn't work on lab machine or my machine
    #I am not using PhantomJS because it didn't work on my machine
    browser = webdriver.Chrome()

    signin(browser, "https://login.yahoo.com/")

    dump_html(browser.page_source, "body")

    #show what happens
    time.sleep(3)

    browser.close()

main()
