#!/usr/bin/python
# enconding: utf-8

"""
@author:merrickzhang
@contact: merrickzhang@126.com
@file: 005.py
@time: 2016/11/6 18:23
"""


a = '250'
b = int(a)

print (b)

a = 520
b = float(a)
print (b)

a = 5.99
b = str(a)
print (b)

c = str(5e99)
print(c)

str = "I Love FishC.com"
print (str)

# 获取类型

a = '520'
b = type(a)
print (b)
b = type(5.2)
print (b)
b = type(True)
print (b)

#判断时指定一个参数的类型
#isinstance()

a = '小甲鱼'
print (a)

在python 3.4.1 shell上行动的
>>> a = '小甲鱼'
>>> print (a)
小甲鱼
>>> isinstance(a, str)
True
>>> isinstance(a, int)
False
>>> isinstance(320, int)
True

>>> isinstance(320.23 ,float)
True
>>> isinstance(322.22, bool)
False











