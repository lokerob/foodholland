# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


class FoodSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ['foodholland.nl']

    def start_requests(self):
        urls = [
            'https://www.foodholland.nl/vacaturebank/home.html?of=0',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parseListOfFoodJobs)

    def parseListOfFoodJobs(self, response):
	#scraping data for variables of interest

	#crawl to detail pages
        try:
            url=response.css('div [id="pagingright"]  a').attrib['href']
            url2="https://www.foodholland.nl"+url
            print(url2)
            yield scrapy.Request(url=url2, callback=self.parseListOfFoodJobs)
        except:
            pass

	#crawling to next list of food jobs
#        try:
#            url=response.css('div [id="pagingright"]  a').attrib['href']
#            url2="https://www.foodholland.nl"+url
#            print(url2)
#            yield scrapy.Request(url=url2, callback=self.parseListOfFoodJobs)
#        except:
#            pass














