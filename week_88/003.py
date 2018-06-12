# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 10:09:00 2018

@author: asiaw
"""

def bfs(i,answer,lenmax,flag,quiet):
    """
        返回i的答案
    """
    if flag[i]:
        return 
    
    if lenmax[i][0] == 0:
        answer[i] = i
        flag[i] = 1
        return 
    max = 5001
    person = 0
    answer[i] = i
    for j in range(1,lenmax[i][0] + 1):
        bfs(lenmax[i][j],answer,lenmax,flag,quiet)
        if max > quiet[answer[lenmax[i][j]]]:
            max = quiet[answer[lenmax[i][j]]]
            person = answer[lenmax[i][j]]
    flag[i] = 1
    if max < quiet[i]:
        answer[i] = person
    return
    

def loudAndRich(richer, quiet):
    """
    :type richer: List[List[int]]
    :type quiet: List[int]
    :rtype: List[int]
    """
    
    answer = quiet[:]
    lenmax = []
    flag = []
    for i in range(len(quiet)):
        lenmax.append([0])
        flag.append(0)
    for i in richer:
        lenmax[i[1]][0] += 1
        lenmax[i[1]].append(i[0])
    for i in range(len(quiet)):
        bfs(i,answer,lenmax,flag,quiet)
    
    for i in answer:
        print(i)
  
richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]      
loudAndRich(richer,quiet)