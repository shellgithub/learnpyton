#!/usr/bin/python
# enconding: utf-8

"""
@author:merrickzhang
@contact: merrickzhang@126.com
@file: turpledemo.py
@time: 2016/10/16 21:47
"""

def add(x,y):
    return x,y,x+y

result = add(10,20)
print result , result[2],result[0],result[1]


x,y,z = add(10,30)
print x,y,z

