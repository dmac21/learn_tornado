# -*- coding: utf-8 -*-
# @Time    : 2018/7/21 下午5:25
# @Author  : dmac
# @Email   : 386501732@qq.com
# @File    : server.py
# @Software: PyCharm

from tornado.httpclient import HTTPClient

def synchronous_visit():
    httpclient=HTTPClient()
    response=httpclient.fetch('http://www.baidu.com')
    print(response.body)

from tornado.httpclient import AsyncHTTPClient

def handle_response(response):
    print(response.body)

def asynchronous_visit():
    httpclient=AsyncHTTPClient()
    httpclient.fetch('http://www.baidu.com',callback=handle_response)



