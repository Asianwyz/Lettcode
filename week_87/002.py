# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:39:56 2018

@author: asiaw
"""

def longestMountain(A):
    """
    :type A: List[int]
    :rtype: int
    """
    
    ans = 0 # 最长‘山脉’长度
    if A[1] > A[0]:        
        count = 2
        flag = True
    else:
        count = 1
        flag = True
    for i in range(2,len(A)):
        if A[i] > A[i-1]:
            if flag:
                count += 1
            else:
                if count > 2 and ans < count:
                    ans == count                    
                count = 1
                flag = True
        elif A[i] < A[i-1]:
            if not flag:
                count += 1
            else:
                if count > 1:
                    count += 1
                    flag = False
    if ans < count:
        ans == count
    
    return ans

A = [2, 1, 4, 7, 3, 2, 5]
print(longestMountain(A))
        