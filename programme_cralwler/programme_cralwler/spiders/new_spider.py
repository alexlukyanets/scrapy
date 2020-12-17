import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class GenSpiderCrawl(CrawlSpider):
    name = 'un_programme_crawler'
    allowed_domains = ['un.org']
    start_urls = ['https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html']

    rules = (Rule(LinkExtractor(allow=('funds-programmes-specialized-agencies-and-others'), deny=('zh/sections', 'fr/sections', 'ru/sections')), callback='parse_page'),)

    def parse_page(self, response):
        list_of_agecies = response.css('div.field-item.even > h4::text').extract()

        for agency in list_of_agecies:
            with open('un_agencies.txt', 'a+', encoding='utf-8') as f:
                f.write(agency + '\n')



