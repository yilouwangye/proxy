# !usr/bin/env python
# -*-coding:utf-8 -*-

# @FileName: proxy.py
# @Author:tian
# @Time:07/04/2020

from db import RedisClient
import sys
import json
import requests
from pyquery import PyQuery as pq

# sys.path.append(r'E:\pycharm\project\scrapy_base\procuration')
# print(sys.path)

def reids_client():
    client = RedisClient()
    choice = client.random()
    return choice

def api():
    response = requests.get('http://localhost:5000/kuaidai/random').text
    doc = pq(response)
    result = doc('div p').text()
    return 'http://{result}'.format(result=result)


if __name__ == '__main__':
    print(api())
