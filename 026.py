# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 18:40:21 2018

@author: asiaw
"""

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0            
    number = nums[0]
    length = 1
    for i in range(1,len(nums)):
        if nums[i] == number:
            continue
        number = nums[i]
        nums[length] = number
        length += 1

    return length
    

nums = [0,0,1,1,1,2,2,3,3,4]
leng = removeDuplicates(nums)
print(leng)
for i in range(leng):
    print(nums[i])

    
    