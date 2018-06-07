# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 13:42:38 2018

@author: asiaw
"""
#Lettcod 020
# 堆栈，先进后出。
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    
    stack = []
    for i in s:
        if i == '(':
            stack.append(1)
        elif i == '[':
            stack.append(2)
        elif i == '{':
            stack.append(3)
        elif i == ')':
            if not stack:
                return False
            index = stack.pop()
            if index != 1:
                return False
        elif i == ']':
            if not stack:
                return False
            index = stack.pop()
            if index != 2:
                return False
        elif i == '}':
            if not stack:
                return False    
            index = stack.pop()
            if index != 3:
                return False
    
    return True

s = "{[]}]"
print(isValid(s))