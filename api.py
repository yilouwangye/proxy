# !usr/bin/env python
# -*-coding:utf-8 -*-

# @FileName: api.py
# @Author:tian
# @Time:07/16/2020


from flask import Flask,g,render_template
from config import *
from db import *
import json

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

def get_conn():
    for proxy in GENERATOR_MAP:
        pass
        if not hasattr(g,proxy):
            setattr(g,proxy,eval('RedisClient()'))
    return g

@app.route('/<proxy>/random')
# The return type must be a string, dict, tuple, Response instance
def random(proxy):
    g = get_conn()
    ip = getattr(g,proxy).random()
    return render_template('randomv1.html',result=ip)

@app.route('/<proxy>/count')
def count(proxy):
    g = get_conn()
    c = getattr(g,proxy).count()
    return json.dumps({'count':c})

if __name__ == '__main__':
    app.run(debug=True)
