#!/usr/bin/python
# enconding: utf-8

"""
@author:merrickzhang
@contact: merrickzhang@126.com
@file: 01lesson03.py
@time: 2016/10/23 20:50
"""


def __handleText(txt):
    print txt

def __handleJSON(json):
    print json

def __handleHTML(html):
    print html

def decoder(type):
    if type=='html':
        return __handleHTML
    if type=='txt':
        return __handleText
    else :
        return __handleJSON

decoder('html')('<p>This is a paragraph</p>')

