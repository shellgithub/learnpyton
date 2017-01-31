#!/usr/bin/python
# enconding: utf-8

"""
@author:merrickzhang
@contact: merrickzhang@126.com
@file: 009--006.py
@time: 2016/11/15 23:19
"""


for i in range(10):
    if i%2 != 0:
        print(i)
        continue
    i += 2
    print(i)

