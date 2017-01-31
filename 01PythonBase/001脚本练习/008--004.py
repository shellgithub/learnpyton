#!/usr/bin/python
# enconding: utf-8

"""
@author:merrickzhang
@contact: merrickzhang@126.com
@file: 008-004.py
@time: 2016/11/15 22:50
"""

#条件表达式（三元操作符）
#有了这个三元操作符的条件表达式，你可以使用一条语句完成 以下的条件判断和赋值操作：

x,y = 4,5
if x < y:
    small = x
else:
    small = y

#例子可以改进为：
small = x if x < y else y

