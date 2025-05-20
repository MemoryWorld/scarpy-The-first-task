import scrapy


class Opp2Spider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/']

    def parse(self, response):
        context = response.xpath('/html/head/title/text()')
        title = context.extract_first()
        print(title)
        pass
