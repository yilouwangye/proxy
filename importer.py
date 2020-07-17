# !usr/bin/env python
# -*-coding:utf-8 -*-

# @FileName: importer.py
# @Author:tian
# @Time:07/04/2020

from db import RedisClient
from kuaidai import KuaidaiProcuration

class ImportDatabase(object):
    def __init__(self):
        self.client = RedisClient()
        self.kuaidai = KuaidaiProcuration()

    def set_ip(self,value):
        self.client.set(value)

    def main(self):
        for item in self.kuaidai.parse_url():
            if item not in self.client.get():
                self.client.set(item)
        print(f'获取IP个数：{self.client.count()}')

if __name__ == '__main__':
    i = ImportDatabase()
    i.main()

