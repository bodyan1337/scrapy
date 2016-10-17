# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BogdanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    laptop = scrapy.Field()
    price = scrapy.Field()
    # images = scrapy.Field()
    image_urls = scrapy.Field()

# class ImageItem(scrapy.Item): 
#     images = scrapy.Field()
#     image_urls = scrapy.Field()