#!/usr/bin/python
# enconding: utf-8

"""
@author:merrickzhang
@contact: merrickzhang@126.com
@file: 010--001list.py
@time: 2016/11/27 15:57
"""


member = ['小甲鱼','小布丁']
print(member[1])

empty = []
print (empty)

member.append('三')
print(member)
print (len(member))

"""
批量添加列表
member.append('four','five')   此方法不能使用
"""
member.extend(['four','five'])
print(member)
print (len(member))

"""在指定位置添加一个列表"""
member.insert(0,'一')
print(member)
print (len(member))

