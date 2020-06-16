# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    Title = scrapy.Field()
    Author = scrapy.Field()
    Price = scrapy.Field()
    image_link = scrapy.Field()
    #books = scrapy.Field()
    



    
