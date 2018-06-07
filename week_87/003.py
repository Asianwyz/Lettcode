# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 10:22:06 2018

@author: asiaw
"""

def isNStraightHand(hand, W):
    """
    :type hand: List[int]
    :type W: int
    :rtype: bool
    """
    
    length = len(hand)
    if length % W != 0:
        return False
    
    hand1 = hand.sort()
    dict = {}
    list = []
    count = 0
    for i in hand1:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
            list[count] = i
            count += 1
    item = 0
    while item == len(list):
        number = list[item]
        for i in range(number, number + W):
            if dict[i]:
                dict[i] -= 1
            else:
                return False
        while not dict[number]:
            item += 1
            number = list[item]
    
    return True
        
hand = [1,2,3,6,2,3,4,7,8]
w = 3
print(isNStraightHand(hand,w))