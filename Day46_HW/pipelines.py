import json
import os

class JsonWriterPipeline:
    def open_spider(self, spider):
        # 建立資料夾
        self.dir_path = 'output'
        os.makedirs(self.dir_path, exist_ok=True)

        # 開啟檔案做準備
        self.file_path = os.path.join(self.dir_path, f'{spider.name}_result.json')
        self.file = open(self.file_path, 'w', encoding='utf-8')
        self.file.write('[\n')  # JSON 陣列起始符號
        self.first_item = True

    def close_spider(self, spider):
        self.file.write('\n]')  # JSON 陣列結尾
        self.file.close()

    def process_item(self, item, spider):
        # 將 item 轉換為 JSON 字串
        line = json.dumps(dict(item), ensure_ascii=False, indent=2)

        # 如果不是第一筆，要加逗號換行
        if not self.first_item:
            self.file.write(',\n')
        else:
            self.first_item = False

        self.file.write(line)
        return item
