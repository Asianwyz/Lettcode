# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 18:18:50 2018

@author: asiaw
"""

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    
    dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4,
            'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
    
    id = 0
    length = len(s)
    count = 0
    while id < length-1:
        if s[id:id+2] in dict:
            count += dict[s[id:id+2]]
            id += 2
        else:
            count += dict[s[id]]
            id += 1
    if id < length:
        count += dict[s[id]]
        
    return count

s = 'MCMXCIV'
print(romanToInt(s))