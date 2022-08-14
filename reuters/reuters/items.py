# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ReutersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()
    title = scrapy.Field()
    summary = scrapy.Field()
    topic = scrapy.Field()


    