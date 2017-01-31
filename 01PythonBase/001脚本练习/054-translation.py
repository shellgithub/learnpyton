#!/usr/bin/python
# enconding:utf-8

"""
@author:merrickzhang
@contact: merrickzhang@126.com
@file:054-translation.py
@time:2017/1/7 06:50
"""

import urllib.request
import urllib.parse
import json
import time

while True
    content = input("请输入需要翻译的内容(输入q!退出程序)：")

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index'
    head = {}
    head[Usr-Agent] = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36']


    data = {}
    data['type'] = content
    data['i'] = 'I love FishC.com!'
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.6'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['typeResult'] = 'true'
    data = urllib.parse.urlencode(data).encode('utf-8')

    response = urllib.request.urlopen(url, data)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))

