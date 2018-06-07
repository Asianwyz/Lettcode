# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 10:50:57 2018

@author: asiaw
"""

def shortestPathLength(graph):
    """
    :type graph: List[List[int]]
    :rtype: int
    """
    flag = []
    for i in len(graph):
        flag.append(0)
        
    flag[0] = 0
    
        