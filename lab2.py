#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 17:57:50 2022

@author: rishabh
"""
import math


def seconds2days(n):
    """ It returns the number of days from seconds """
    d = n / 86400
    return d


def box_surface(a, b, c):
    """ It returns the surface area of a cuboid """
    A = 2 * a * b + 2 * a * c + 2 * b * c
    return A


def triangle_area(a, b, c):
    """ It returns the area of a triangle"""
    s = (a + b + c) / 2
    Area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return Area
