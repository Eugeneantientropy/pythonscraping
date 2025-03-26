import scrapy
from scrapy_demo.items import ScrapyDemoItem

class PttSpider(scrapy.Spider):
    name = "ptt"
    allowed_domains = ["ptt.cc"]

    def start_requests(self):
        board = self.settings.get('BOARD_NAME')
        url = f"https://www.ptt.cc/bbs/{board}/index.html"
        yield scrapy.Request(url, cookies={'over18': '1'}, callback=self.parse)

    def parse(self, response):
        # 抓首頁前面幾篇文章連結
        posts = response.xpath('//div[@class="r-ent"]/div[@class="title"]/a')
        for post in posts:
            post_url = response.urljoin(post.xpath('@href').get())
            yield scrapy.Request(post_url, cookies={'over18': '1'}, callback=self.parse_post)

    def parse_post(self, response):
        item = ScrapyDemoItem()
        item['title'] = response.xpath('//meta[@property="og:title"]/@content').get()
        item['author'] = response.xpath('//span[@class="article-meta-value"][1]/text()').get()
        item['date'] = response.xpath('//span[@class="article-meta-value"][3]/text()').get()
        content = response.xpath('//*[@id="main-content"]/text()').getall()
        item['content'] = ''.join([line.strip() for line in content if line.strip()])
        yield item
