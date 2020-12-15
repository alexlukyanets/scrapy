import scrapy

filename = 'book_titles.txt'


class IntroSpider(scrapy.Spider):
    name = "intro_spider"

    def start_requests(self):
        urls = [
            'https://books.toscrape.com/catalogue/page-1.html',
            'https://books.toscrape.com/catalogue/page-2.html',
            'https://books.toscrape.com/catalogue/page-3.html',
            'https://books.toscrape.com/catalogue/page-4.html',
            'https://books.toscrape.com/catalogue/page-5.html',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        book_list = response.css('article.product_pod > h3 > a::attr(title)').extract()

        with open(filename, 'a+') as f:
            for book_title in book_list:
                f.write(book_title + "\n")
