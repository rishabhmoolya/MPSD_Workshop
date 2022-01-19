#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 21:44:40 2022

@author: user
"""
    
def count_sub_in_file(filename, s):
    try:
     f = open(filename, 'r')
    except FileNotFoundError:
     return -1  
    lines = f.readlines()
    #y = []
    for elem in lines:
        y = elem.split() 
        #print (y)
        w = 0
        for s in y:
            w = w + y.count(s)
        return w
    
    

    
