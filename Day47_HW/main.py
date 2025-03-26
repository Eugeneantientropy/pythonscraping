# main.py
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    # 檢查參數
    if len(sys.argv) != 3:
        print("用法：python main.py <板名> <檔名.json>")
        print("範例：python main.py Gossiping gossip.json")
        sys.exit(1)

    board = sys.argv[1]
    filename = sys.argv[2]

    # 動態設定
    settings = get_project_settings()
    settings.set('BOARD_NAME', board)
    settings.set('FEED_URI', f'output/{filename}')
    settings.set('FEED_FORMAT', 'json')
    settings.set('FEED_EXPORT_ENCODING', 'utf-8')

    process = CrawlerProcess(settings)
    process.crawl('ptt')  # 爬蟲名稱
    process.start()
