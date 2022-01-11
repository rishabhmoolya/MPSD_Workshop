#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 21:37:42 2022

@author: rishabh
"""

import math


def swing_time(L):
    """"It computes the swing time of a given length L. """
    g = 9.81
    t = (2 * math.pi) * math.sqrt(L / g)
    return t


def range_squared(n):
    """"It computes the square of the passed variable """
    y1 = []
    if n > 0:
        for i in range(0, n):
            y = i**2
            y1.append(y)
        return y1
    elif n == 0:
        return list()


def count(element, seq):
    """"It returns the count of elements in the sequence"""
    z = seq.count(element)
    return z
