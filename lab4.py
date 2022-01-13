# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 23:02:47 2022

@author: Moin
"""

import math
import numpy as np


def seq_sqrt(xs):
    s1 = []
    for i in range(len(xs)):
        if xs[i] > 0:
            s = math.sqrt(xs[i])
            s1 = np.append(s1, s)
        else:
            break
    print(s1)


def mean(xs):
    s1 = []
    s = 0
    for i in range(len(xs)):
        s = s + xs[i]
        avg = s/len(xs)

    print(avg)


def wc(filename):
    with open(filename, 'r') as f:   
        lines = f.readlines()
    y1 = 0
    for elem in lines:
        y = elem.split()
        if len(y) > 0:
           y1 = y1 + len(y) 
           #y1.append(len(y))
    print(y1)
