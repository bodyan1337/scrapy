# -*- coding: utf-8 -*-
from scraping.items import BogdanItem
from scrapy.spiders import CrawlSpider, Rule
import scrapy
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.loader import ItemLoader
from scrapy.http.request import Request
from scrapy.item import Item

class PriceSpider(CrawlSpider):
    name = "price"
    allowed_domains = ["price.ua"]
    start_urls = [
        "http://price.ua/catc839t14/page.html"
    ]
    # rules = (
    #     Rule(SgmlLinkExtractor(allow=(".",)), callback='parse', follow=True),        
    # )

    def parse(self, response):
        item = BogdanItem()
        for sel in response.xpath('//div[@class="white-wrap clearer-block"]'):
            name = sel.xpath("//div[@class='info-wrap']/a/text()").extract()
            price = [ ''.join([j for j in i if j.isdigit()]) for i in sel.xpath("//div[@class='price-wrap']/span/text() | //div[@class='price-wrap']/a/text()").extract() if i != " "]
            image = [ s for s in sel.xpath("//div[@class='photo-wrap']//a//span/img/@src | //div[@class='photo-wrap']//a//span/img/@data-original").extract() if s != '/images/preload.gif'] 
        for item['laptop'],item['price'],item['image_urls'] in zip(name,price,image):
            if item['price']:
                item['price'] = int(item['price'])
                if item['price'] < 5000 and item['price'] > 4000:
                    item['price'] = str(item['price'])
                    item['image_urls'] = str(item['image_urls'])
                    yield item
        print "==========228============"
    

        page_end = int(response.xpath('//span[@id="top-paginator-max"]/text()').extract()[0]) 
        category = response.request.url[:26]
        
        count = int(response.xpath('//li[@class="page selected"]/span/text()').extract()[0])
        if count <= page_end:
            next_page_url = category + "/page" + str(count+1) + ".html"
            request = scrapy.Request(url=next_page_url)
            yield request
