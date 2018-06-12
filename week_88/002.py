# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 09:55:42 2018

@author: asiaw
"""

def maxDistToClosest(seats):
    """
    :type seats: List[int]
    :rtype: int
    """
    flag = False
    flag1 = False
    max = 0
    count = 0
    if seats[0] == 0:
        flag = True
        count += 1
        flag1 = False
    for i in range(1,len(seats)):
        if seats[i]:
            if flag:
                max = count
                flag = False
            else:
                if max < (count + 1 ) // 2 :
                    max = (count + 1) // 2
            count = 0
            flag1 = True
        else:
            if flag1:
                flag1 = False
                count = 1
            else:
                count += 1
                if i == len(seats) - 1:
                    if max < count:
                        max = count
    
    return max

seats = [1,0,0,1]
print(maxDistToClosest(seats))
                
        
    
        