# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class WeixinMomentItem(scrapy.Item):
    """
    朋友圈Item
    """
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()  #日期
    moment = scrapy.Field()  #朋友圈文字
    #dict_w=scrapy.Field()
