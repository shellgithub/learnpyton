#!/usr/bin/python
# enconding:utf-8

"""
@author:merrickzhang
@contact: merrickzhang@126.com
@file:054.py
@time:2017/1/7 06:37
"""


import urllib.request

response = urllib.request.urlopen('http://placekitten.com/g/500/600')
cat_img = response.read()

with open('cat_500)600.jpg', 'wb') as f:
    f.write(cat_img)



