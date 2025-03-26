import scrapy
from scrapy_demo.items import ScrapyDemoItem  

class EttodaySpider(scrapy.Spider):
    name = "ettoday"
    allowed_domains = ["ettoday.net"]
    start_urls = ["https://www.ettoday.net/"]

    def parse(self, response):
        articles = response.xpath('//a[starts-with(@href, "https://www.ettoday.net/news/")]')

        for article in articles:
            title = article.xpath('text()').get()
            url = article.xpath('@href').get()
            if title and url:
                item = ScrapyDemoItem()
                item['title'] = title.strip()
                item['url'] = url
                yield item  # 讓 Scrapy 自動幫我們儲存
