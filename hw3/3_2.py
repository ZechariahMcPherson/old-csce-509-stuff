#Creator: Gregory Zechariah McPherson
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import sys

def open_url_write_links(urlToOpen, writeFile):
    """"opens url and writes the links on the webpage to file"""
    html = urlopen(urlToOpen)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll('a', href=True):
        writeFile.write(link.attrs['href']+"\n")

def create_output_file():
    """"creates output file"""
    if os.path.isfile("allLinks.txt"):
        os.remove("allLinks.txt")
    newFile = open("allLinks.txt","w+")

    return newFile

def main():
    """calls the functions to write all links"""
    urlToOpen = "https://cse.sc.edu/"
    writeFile = create_output_file()
    open_url_write_links(urlToOpen, writeFile)

main()


