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
        #scraping data for each list item on index page
        for li in response.css('#vacatures li '):
            #scraping data for variables of interest on index page of a list item
#            yield{
    #                response.css('div [id="vacatures"] li a ').attrib['href']
    #                response.css('div.datumlijst div.lijst li a').extract()
    #                response.css('#vacatures li ').xpath('normalize-space()').extract()
#                'url': li.css('a').attrib['href'],
#                'text': li.xpath('normalize-space()').extract(),
#            }
            #crawling to detail page of a list item
#            url=response.css('div [id="vacatures"] li a ').attrib['href']
            url=li.css('a').attrib['href']
            url2="https://www.foodholland.nl"+url
            yield scrapy.Request(url=url2, callback=self.parseDetailPage)

    	#crawl to next index page
        try:
            url=response.css('div [id="pagingright"]  a').attrib['href']
            url2="https://www.foodholland.nl"+url
            print(url2)
            yield scrapy.Request(url=url2, callback=self.parseListOfFoodJobs)
        except:
            pass

    def parseDetailPage(self, response):
        yield{
            'url': response.url,
            'bedrijf': response.css('div.specs h1:nth-of-type(1)').xpath('normalize-space()').extract(),
            'functietitel': response.css('div.specs h1:nth-of-type(2)').xpath('normalize-space()').extract(),
            'locatie': response.css('div.specs h4').xpath('normalize-space()').extract(),
            'text': response.css('#vacatures ::text').extract(),
            'text2': response.xpath('normalize-space(//*[@id="vacatures"])').extract(),
        }

	#crawling to next list of food jobs
#        try:
#            url=response.css('div [id="pagingright"]  a').attrib['href']
#            url2="https://www.foodholland.nl"+url
#            print(url2)
#            yield scrapy.Request(url=url2, callback=self.parseListOfFoodJobs)
#        except:
#            pass














