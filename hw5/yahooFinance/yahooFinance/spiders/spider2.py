#Creator: Gregory Zechariah McPherson
import scrapy
import csv
import re
import os
from bs4 import BeautifulSoup
from scrapy.http import HtmlResponse
from scrapy.selector import Selector
from scrapy.selector import HtmlXPathSelector

"""
The EPS (TTM), Earnings Date, Dividend & Yield, Ex-Dividend Date, and 1y Target Est feilds are loaded after the page is loaded. Scrapy only gets the initial data. This means that I get N/A on all of those fields. I couldn't find a solution on how to change this.
"""

class scrapeMultiplePages(scrapy.Spider):
    name = "multiPages"

    def start_requests(self):
        """does a request for each company url"""

        #sets name for csv file
        outputFile = "multiPages.csv"

        #creates csv file
        if os.path.isfile(outputFile):
            os.remove(outputFile)
        writeFile = open(outputFile,"w+")
        writeFile.close

        #list of companies we are scraping
        companies = ["FB", "XOM", "STX", "NFLX", "AMZN"]

        #opens each company's page
        for company in companies:
            yield scrapy.Request("http://finance.yahoo.com/quote/" + company + "/?p=" + company)

    def parse(self, response):
        """gets table data and writes to csv"""
        regex = re.compile('(?:\?p=)(\w*)')
        company = regex.findall(response.url)

        #sets up csv file
        csvFile = open("multiPages.csv", 'a', newline='', encoding='utf-8')
        writer = csv.writer(csvFile)

        #set header as company name
        header = []
        header.append(company[0])
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

        #Empty row separator between tables
        writer.writerow("")

        csvFile.close()
