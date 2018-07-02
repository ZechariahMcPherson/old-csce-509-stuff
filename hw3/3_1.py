#Creator: Gregory Zechariah McPherson
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://cse.sc.edu/")
bsObj = BeautifulSoup(html, "html.parser")
linkCount = 0
for link in bsObj.findAll('a', href=True):
    linkCount = linkCount + 1
    print("link: " + link.attrs['href'])
print(linkCount)
