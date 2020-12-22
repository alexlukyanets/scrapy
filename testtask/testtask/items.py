# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TesttaskItem(scrapy.Item):
    permit_number = scrapy.Field()
    permit_type = scrapy.Field()
    application_date = scrapy.Field()
    issue_date = scrapy.Field()
    street = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    description = scrapy.Field()
    fee = scrapy.Field()
    contacts = scrapy.Field()
    cost = scrapy.Field()