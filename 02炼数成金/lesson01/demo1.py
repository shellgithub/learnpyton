#!/usr/bin/python
# enconding: utf-8

"""
@author:merrickzhang
@contact: merrickzhang@126.com
@file: demo2.py
@time: 16-9-27 9:07
"""

import numpy

def sigmoid(x):
    if x < -709:
        x = -709

    if x > 28.0:
        x = 28.0
    return 1.0 / (1 + exp(-x))

if __name__ == '__main__':
    print(sigmoid(1000))

