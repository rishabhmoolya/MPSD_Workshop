#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 17:10:29 2022

@author: rishabh
"""

import math


def box_volume(a, b, c):
    """ It returns the volume of a box """
    vol = a * b * c
    return vol


def fall_time(h):
    """ It returns the time needed for an object falling from a height h """
    g = 9.81
    t = math.sqrt((2 * h)/g)
    return t


# =============================================================================
# def interval_point(a, b, x):
#     """ It returns how far to go towards b starting at a """
#     return
# =============================================================================

def impact_velocity(h):
    """It returns the velocity of an object"""
    g = 9.81
    v = g * fall_time(h)
    return v


def signum(x):
    """ It returns 1 if x>0, 0 if x=0, -1 if x <0 """
    if x == 0:
        return 0
    elif x > 0:
        return 1
    elif x < 0:
        return -1
