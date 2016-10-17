# -*- coding: utf-8 -*-
import sys
import MySQLdb
import hashlib
from scrapy.exceptions import DropItem
from scrapy.http import Request
import scrapy
from scrapy.conf import settings
from cStringIO import StringIO
from scrapy.contrib.pipeline.images import ImagesPipeline, ImageException
#import psycopg2
# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class MySQLStorePipeline(object):

    def __init__(self):
#        self.conn = MySQLdb.connect(user='root', '1577292', 'priceua', '127.0.0.1', charset="utf8", use_unicode=True)
        self.conn = MySQLdb.connect(user='root', passwd='12345678', db='flask', host='localhost', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

#class TutorialPipeline(object):
#    def process_item(self, item, spider):
#        return item

    def process_item(self, item, spider):
        print "========>>>>item[name]", item['laptop']

        try:
            a = "INSERT INTO prices (laptop,price,image)  VALUES (%s, %s, %s)"
            b = (item['laptop'].encode('utf-8'), item['price'].encode('utf-8'), item['image_urls'].encode('utf-8'))
            self.cursor.execute(a,b)

            self.conn.commit()
    

        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])


        return item
    
class MyImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return Request(item['image_urls']) 
        
    # def item_completed(self, results, item, info):
    #     item['images'] = [x for ok, x in results if ok]
    #     return item
    
    # # Override the convert_image method to disable image conversion    
    # def convert_image(self, image, size=None):
    #     buf = StringIO()        
    #     try:
    #         image.save(buf, image.format)
    #     except Exception, ex:
    #         raise ImageException("Cannot process image. Error: %s" % ex)

        # return image, buf    
        
    # def image_key(self, url):
    #     image_guid = hashlib.sha1(url).hexdigest()
    #     return 'full/%s.jpg' % (image_guid)    
