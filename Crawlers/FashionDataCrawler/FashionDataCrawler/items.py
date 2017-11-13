# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FashiondatacrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name= scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    size = scrapy.Field()
    color = scrapy.Field()
    details = scrapy.Field()
    designer = scrapy.Field()
    image_urls = scrapy.Field()
    gender= scrapy.Field()
