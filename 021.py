# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 23:38:38 2018

@author: asiaw
"""

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    
    length1 = len(l1)
    length2 = len(l2)
    list = []
    x, y = 0, 0
    while x < length1 and y < length2:
        if l1[x] > l2[y]:
            list.append(l2[y])
            y += 1
        else:
            list.append(l1[x])
            x += 1
    while x < length1:
        list.append(l1[x])
        x += 1
    while y < length2:
        list.append(l2[y])
        y += 1
        
    return list

l1 = [1,2,4]
l2 = [1,3,4]
print(mergeTwoLists(l1,l2))