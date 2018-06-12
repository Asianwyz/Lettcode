# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 09:36:59 2018

@author: asiaw
"""

def shiftingLetters(S, shifts):
    """
    :type S: str
    :type shifts: List[int]
    :rtype: str
    """
    ss = ''
    leng = len(shifts) - 2
    while leng>=0:
        shifts[leng] += shifts[leng+1]
        leng -= 1
       
    for i in range(0,len(S)):
        displace = shifts[i] % 26
        length = ord(S[i]) + displace
        if length > 122:
            length = length - 122 + 96
        ss += chr(length)

    return ss


s = 'abc'
shifts = [3,5,9]
print(shiftingLetters(s,shifts))
    