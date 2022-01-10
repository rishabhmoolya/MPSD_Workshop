# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:10:30 2022

@author: Gargi, Moiunddin, Rishabh
"""

def distance(a,b):
    '''This function returns the distance between two numbers.'''
    x = abs(b-a)
    return x

def geometric_mean(a,b):
    '''It returns the GM of two numbers'''    
    y = (a*b)**0.5
    return y

def pyramid_volume(A,h):
    '''It returns the volume of a pyramid with base area A and height H.'''
    z = (A*h)/3
    return z
    