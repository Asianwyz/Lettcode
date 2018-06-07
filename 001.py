# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 10:23:42 2018

@author: asiaw
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dic = {}
    for i, num in enumerate(nums):
        if num in dic:
            return [dic[num], i]
        else:
            dic[target - num] = i

        
        
nums = [3, 3]
target = 6
print(twoSum(nums, target))