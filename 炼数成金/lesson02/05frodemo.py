#!/usr/bin/python
# enconding: utf-8

"""
@author:merrickzhang
@contact: merrickzhang@126.com
@file: 05frodemo.py
@time: 2016/10/16 22:27
"""
# x = range(1,10)
# for i in x:
#     print i
#

x = range(1,7)
y = [i**2 for i in x]
print y

z = [i**2 if i<3 else i**3 for i in x]
print x
print z

x = range(1,10)
y = xrange(1,10)
print x,y



