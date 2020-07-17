# !usr/bin/env python
# -*-coding:utf-8 -*-

# @FileName: process.py
# @Author:tian
# @Time:07/04/2020

import requests
from kuaidai import KuaidaiProcuration
from db import RedisClient
import random
from requests.exceptions import ConnectionError,RequestException
import time

class VaildTester(object):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    def __init__(self):
        self.client = RedisClient()

    def test(self,value):
        raise  NotImplementedError

    def run(self):
        items = self.client.get()
        for item in items:
            self.test(item)

class IpVailTester(VaildTester):
    def __init__(self):
        VaildTester.__init__(self)

    def test(self,value):
        print(f'正在测试IP地址:{value}')
        try:
            test_url = 'http://quotes.toscrape.com/'
            proxies = {'http':'http://' + value}
            response = requests.get(test_url,proxies=proxies)
            if response.status_code == 200:
                print(f'ip:{value} 有效')
                print(response.text[0:100])
        except ConnectionError as e:
            print(f'ip:{value} 失效')
            self.client.delete(value)
            print(f'ip:{value} 已删除！')
            print(e)

if __name__ == '__main__':
    IpVailTester().run()




