# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 12:40:42 2018

@author: asiaw
"""

def reverse(x):
    """
    :type x: int
    :rtype: int
    """

    if x < 0:
        y = -1
        x *= -1
    else:
        y = 1
        
    z = int(str(x)[::-1]) * y
    if z > 2**32 -1 or z < 2**32 *-1:
        return 0
    else:
        return z

x = 120
print(reverse(x))
