#!/usr/bin/python
# enconding: utf-8

"""
@author:merrickzhang
@contact: merrickzhang@126.com
@file: funcdemo1.py
@time: 2016/10/23 21:12
"""


def add(a,b,c):
    return a+b+c
#
# print add(10,20,30)
#
# print add(10,c=20,b=40)
#
# def add(*args):
#     return sum(args)*2
#
# print add(10,20,30)

# x = [1,2,34]
# add(x[0],x[1],x[2])
# add(*x)
# print add(*x)
#
# y = {'a':10,'b':20,'c':30}
# add(y['a'],y['b'],y['c'])
#
# add(**y)


def add(*args):
    return sum(args)
print add(10,20,30,40,1,2,3,4)

def add(**kwargs):
    return sum(kwargs.values())

print add(a=10,b=20,c=30,d=40,e=5)












