# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 10:41:12 2022

@author: Moin
"""
import urllib.request

def line_averages(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        #print(lines)
    for line in lines:
        s = 0
        for elem in line.split(','):
            s = s + int(elem)
            avg = s/len(line.split(','))
        print(avg)


def noaa_string():
    """Fetch from the Internet and return the current NOAA METAR
    weather observation data for EDDH (Hamburg Airport) as a string.
    """
    url = "http://tgftp.nws.noaa.gov/data/observations/metar/decoded/EDDH.TXT"
    noaa_data_string = urllib.request.urlopen(url).read()
    return noaa_data_string.decode("utf-8")


# =============================================================================
# def noaa_temperature(s):
#     # s = noaa_string()
#     # lines = s.read()
#     y = s.split()
# #     for i in range(len(s)):
#     if y == 'Temperature:':
#         
#     print(y)
# 
# =============================================================================
