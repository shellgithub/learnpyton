#!/usr/bin/python
# enconding: utf-8

"""
@author:merrickzhang
@contact: merrickzhang@126.com
@file: 011--001list.py
@time: 2016/11/29 22:10
"""

"""数据交换"""
member = ['小甲鱼','小布丁']
print(member)

temp = member[0]
member[0] = member[1]
print(member)
member[1] = temp
print(member)


"""从列表删除元素
remove('')   只需要知道值的内容，不需要知道位置，此值是必须存在的
"""
member.remove('小布丁')
print(member)
"""
member.remove('一')
"""
"""只需要知道值的内容，不需要知道位置，此值是必须存在的"""
member = ['小甲鱼','小布丁']
del member[0]
print(member)
'''del member
print(member)
'''

"""pop()默认从最后一个开始删除"""
member = ['小甲鱼','小布丁','一','二','三','四']
member.pop()
print(member)
name = member.pop()
print(member)
name = member.pop(1)
print(member)


'''列表分片
利用索引值，每次
'''
member = ['小甲鱼','小布丁','一','二','三','四']
print(member[1:3])
'''从第2个值开始，第3个之前结束，打印出来的值为：['小布丁', '一']'''

print(member[:3])

'''获取列表的拷贝'''
print(member[:])


