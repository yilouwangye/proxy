# !usr/bin/env python
# -*-coding:utf-8 -*-

# @FileName: kuaidai.py
# @Author:tian
# @Time:07/04/2020

import requests
from pyquery import PyQuery as pq
from config import *
from requests.exceptions import RequestException
import time

class KuaidaiProcuration(object):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'Host': 'www.kuaidaili.com'
    }
    def __init__(self):
        pass

    def get_ip(self,url):
        response = requests.get(url,headers=self.headers)
        if response.status_code == 200:
            try:
                doc = pq(response.text)
                results = doc('.table-bordered tbody tr')
                for result in results.items():
                    items = result.find('td[data-title="IP"]').text() + ':' + result.find('td[data-title="PORT"]').text()
                    yield items
            except RequestException as e:
                print(e)
        else:
            return None

    def parse_url(self):
        for i in range(1,MAX_PAGE + 1):
            url = 'https://www.kuaidaili.com/free/intr/' + str(i) +'/'
            # print(url)
            time.sleep(2)
            for item in self.get_ip(url):
                yield item
                print(item)

if __name__ == '__main__':
    k = KuaidaiProcuration()
    k.parse_url()

