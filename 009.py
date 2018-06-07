# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 14:16:41 2018

@author: asiaw
"""

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    if x < 0:
        return False
    
    y = str(x)
    s1 = y[:len(y) // 2]
    if len(y) % 2:
        s2 = y[len(y) // 2 + 1:]
    else:
        s2 = y[len(y) // 2:]
    s2 = s2[::-1]
    if s1 == s2:
        return True
    else:
        return False
    
x = 1234321
print(isPalindrome(x))