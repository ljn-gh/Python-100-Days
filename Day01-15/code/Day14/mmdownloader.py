from time import time
from threading import Thread

import requests


class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('/Users/Hao/Downloads/' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=772a81a51ae5c780251b1f98ea431b84&num=10')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    if data_model.get('code') == 200:
        for mm_dict in data_model['newslist']:
            url = mm_dict['picUrl']
            # 通过多线程的方式实现图片下载
            DownloadHanlder(url).start()


if __name__ == '__main__':
    main()
