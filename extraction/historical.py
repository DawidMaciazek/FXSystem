import scrapy
from scrapy.crawler import CrawlerProcess

def histdata(pair):
    start_loc = "http://www.histdata.com/download-free-forex-data/?/ascii/1-minute-bar-quotes"

    class base_spider(scrapy.Spider):
        name = "quotes"

        def start_requests(self):
            urls = [start_loc]
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

        def parse(self, response):
            response

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(MySpider)
    process.start()
