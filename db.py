# !usr/bin/env python
# -*-coding:utf-8 -*-

# @FileName: db.py
# @Author:tian
# @Time:07/04/2020

import redis
from config import *
import random

class RedisClient(object):
    def __init__(self,host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD):
        '''

        :param host:
        :param port:
        :param password:
        '''
        self.db = redis.StrictRedis(host=host,port=port,password=password,decode_responses=True)

    def name(self):
        return DB_NAME

    def set(self,value):
        return self.db.rpush(self.name(),value)

    def get(self):
        return self.db.lrange(self.name(),0,-1)

    def random(self):
        return random.choice(self.get())

    def delete(self,value):
        return self.db.lrem(self.name(),0,value)

    def pop(self,value):
        return self.db.lrem(self.name(),-1,value)

    def count(self):
        return self.db.llen(self.name())

if __name__ == '__main__':
    r = RedisClient()
    print(r.get())




