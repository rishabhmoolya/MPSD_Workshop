#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 18:28:52 2022

@author: moolyari
"""

import math


def degree(x):
    """ It takes the value in radians and returns the converted
    value in degrees."""
    theta = x * 360 / (2 * math.pi)
    return theta


def min_max(m):
    """ It computes the minimum of the elements and returns the maxium value
    of the elements in the form of a tuple"""
    xmin = min(m)
    xmax = max(m)
    return (xmin, xmax)


def geometric_mean(xs):
    """"It computes the geometric mean of the numbers given in the list xs. """
    for i in range(len(xs)):
        gm = (xs[i] * xs[i + 1])**(1 / len(xs))
        return gm
