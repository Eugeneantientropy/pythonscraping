import scrapy
from scrapy_demo.items import ScrapyDemoItem  


class PttSpider(scrapy.Spider):
    name = "ptt"
    allowed_domains = ["ptt.cc"]
    start_urls = ["https://www.ptt.cc/bbs/CarShop/M.1742956305.A.65B.html"]

    def parse(self, response):
        # 初始化 item
        item = ScrapyDemoItem()

        # 抓標題
        item['title'] = response.xpath('//meta[@property="og:title"]/@content').get()

        # 抓作者
        item['author'] = response.xpath('//span[@class="article-meta-value"][1]/text()').get()

        # 抓發文時間
        item['date'] = response.xpath('//span[@class="article-meta-value"][3]/text()').get()

        # 抓內文（會先移除文章資訊的那幾段）
        main_content = response.xpath('//*[@id="main-content"]/text()').getall()
        item['content'] = ''.join([line.strip() for line in main_content if line.strip()])

        yield item
