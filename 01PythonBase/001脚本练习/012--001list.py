#!/usr/bin/python
# enconding: utf-8

"""
@author:merrickzhang
@contact: merrickzhang@126.com
@file: 012--001list.py
@time: 2016/11/29 22:28
"""
''''
列表比较大小
'''
list1 = [123]
list2 = [234]
print(list1 > list2)

list1 = [123,456]
list2 = [234,123]
print(list1 > list2)

list3 = [123,456]
print((list1 < list2) and (list1 == list3))

list4 = list1 + list2
print(list4)


print(list3*3)

list3 *= 5
print(list3)

print('一' not in list3)


list5 = [123,['三','四'],456]
print(list5)
'''三在list5的子列表的1个'''
print('三' not in list5)
print('三' not in list5[1])
print(list5[1][1])

'''查看list方法有哪些'''
print(dir(list))
'''
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
'''
'''查看123在list3中出现多少次'''
print(list3.count(123))
'''查看123在list3第0次出现的位置'''
print(list3.index(123))
'''查看123在list3第0次出现的位置,从第3个开始，第7个结束计算'''
print(list3.index(123,3,7))


list6 = ['1','2','43','12','453']
print(list6)
list6.reverse()
print(list6)
list6.sort()
print(list6)

'''sort排序，内部翻转'''
list6.sort(reverse=True)
print(list6)

list6 = ['1','2','43','12','453']
list7 = list6[:]
list8 = list6
list6.sort()
print(list6)
'''list7的值和原来的一样'''
print(list7)
'''list8相当是list6的软链接'''
print(list8)






























