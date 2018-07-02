#Creator: Gregory Zechariah McPherson
#I used the book pages 75-76
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import csv
#ensures url opens correctly
try:
    html = urlopen("https://cse.sc.edu/~matthews/Courses/590/Resources/sched.html")

except HTTPError as e:
    print(e)

except URLError as e:
    print ("The server could not be found!")

#ensures there are no BeautifulSoup problems
try:
    bsObj = BeautifulSoup(html, "html.parser", from_encoding="iso-8859-1")
    masterSchedule = bsObj.findAll("table", class_="datadisplaytable")[0]
    listOfRows = masterSchedule.findAll("tr")

except AttributeError as e:
    print(e)

#makes sure there are no IO errors
try:
    #I had to make this utf-8 for HTML entities eg &nbsp
    #you have to tell excel this is a utf-8 csv otherwise the data looks weird
    csvFile = open("schedFromScraper.csv", 'wt', newline='', encoding='utf-8')
    writer = csv.writer(csvFile)

except IOError:
    print("Error creating file")

#writes data to CSV file
try:
    for row in listOfRows:
        csvRow = []
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)

finally:
    csvFile.close()
