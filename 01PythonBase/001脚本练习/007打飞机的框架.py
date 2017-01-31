#!/usr/bin/python
# enconding: utf-8

"""
@author:merrickzhang
@contact: merrickzhang@126.com
@file: 007.py
@time: 2016/11/6 19:07
"""


#也不起的分支和循环

#打飞机的框架

加载背景音乐
播放背景音乐（设置单曲循环）
我方飞机诞生
interval = 0

wile True:
    if 用户是否点击了关闭按钮：
            退出程序

    interval + = 1
    if interval == 50:
        interval = 0
        小飞机诞生

    小飞机移动一个位置
    屏幕刷新

    if 用户鼠标产生移动：
        我方飞机中心位置 = 用户鼠标位置
        屏幕刷新

    if 我方飞机与小飞机发生肢体冲突：
        我方挂，播放撞机音乐
        修改我方飞机图案
        打印“Game over”
        停止背景音乐，最好淡出

