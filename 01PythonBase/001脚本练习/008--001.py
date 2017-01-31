#!/usr/bin/python
# enconding: utf-8

"""
@author:merrickzhang
@contact: merrickzhang@126.com
@file: 008--002.py.py
@time: 2016/11/6 19:31
"""



score = int(input("请输入一个分数："))
if 100 >= score >= 90:
    print('A')
if 90 > score >= 80:
    print('B')
if 80 > score >= 60:
    print('C')
if 60 > score >=0:
    print('D')
if score < 0 or score > 100:
    print('输入错误！')
