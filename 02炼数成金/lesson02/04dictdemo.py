#!/usr/bin/python
# enconding: utf-8

"""
@author:merrickzhang
@contact: merrickzhang@126.com
@file: dictdemo.py
@time: 2016/10/16 21:58
"""

x = [1,2,3,4,5]
y = '12345'


#hash(x)
print hash(y)

z = {'name':'zhang','age':30,'sex':'m'}
print z

# z = dict(name='zhang',age=30,sex='m')
# print z
#
# print z['name']
#
# # print z['loc']
# print 'loc' in z
# print 'age' in z
#
# for (k,v) in z.items():
#     print k+'='+str(v)
#
# print z.keys()
# print z.values()
#
# print z.get('loc',None)
#
# print z.setdefault('loc','ShangHai')

m = {'abc':1,'def':2}
print m
zup = z.update(m)
print zup


