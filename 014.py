# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 13:14:59 2018

@author: asiaw
"""
# 用二分的方法确定前缀，再循序确定是否是每个字符串的前缀。O（nlogn)

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    
    
    strs.sort()
    if len(strs):
            length = len(strs[0])
    else:
        return ""
    l, r = 0, length -1
    mid = (l + r) // 2
    prefix = ""
    while l <= r:
        pre = strs[0][:mid+1]
        flag = True
        for i in strs:
            if i[:mid+1] == pre:
                continue
            else:
                r = mid -1
                flag = False
        if flag:
            if len(prefix) < len(pre):
                prefix = pre
            l = mid + 1
        mid = (l + r) // 2
        
    return prefix
    
strs = ["ca","a"]
print(longestCommonPrefix(strs))