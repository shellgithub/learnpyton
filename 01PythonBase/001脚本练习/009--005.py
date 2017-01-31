#!/usr/bin/python
# enconding: utf-8

"""
@author:merrickzhang
@contact: merrickzhang@126.com
@file: 009--005.py
@time: 2016/11/15 23:14
"""

bingo = "小甲鱼是帅哥"
answer = input('请输入小甲鱼最想听的一句话：')

while True:
    if answer == bingo:
        break
    answer = input('抱歉，错了，请重新输入：')
print('回答对了')