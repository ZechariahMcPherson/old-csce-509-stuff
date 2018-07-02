#Creator: Gregory Zechariah McPherson
import scrapy
import csv
from bs4 import BeautifulSoup
from scrapy.http import HtmlResponse
from scrapy.selector import HtmlXPathSelector

"""
The EPS (TTM), Earnings Date, Dividend & Yield, Ex-Dividend Date, and 1y Target Est feilds are loaded after the page is loaded. Scrapy only gets the initial data. This means that I get N/A on all of those fields. I couldn't find a solution on how to change this.
"""

class scrapeFB(scrapy.Spider):
    name = "fb"
    start_urls = ["http://finance.yahoo.com/quote/FB?p=FB"]

    def parse(self, response):
        """gets table data and writes to csv"""

        #csv file
        csvFile = open("scrapeFB.csv", 'wt', newline='', encoding='utf-8')
        writer = csv.writer(csvFile)

        #set header as company name
        header = []
        header.append("FB")
        writer.writerow(header)

        hxs = HtmlXPathSelector(response)

        #iterates through the two tables
        for table in hxs.select("//div[@id='quote-summary']/div"):

            #iterates through each row and puts the data in a csv
            for row in table.xpath('.//tr'):
                csvRow = []

                #iterates through tds and appends to csvRow array
                for td in row.xpath('.//td'):

                    text = td.xpath('.//text()').extract()

                    csvRow.append(text[0])

                writer.writerow(csvRow)


        csvFile.close()
