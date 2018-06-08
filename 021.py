# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 23:38:38 2018

@author: asiaw
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        chain = ListNode(0)
        top = chain
        while l1 and l2:
            if  l1.val > l2.val:
                #new = ListNode(l2.val)
                chain.next = l2
                l2 = l2.next
            else:
                #new = ListNode(l1.val)
                chain.next = l1
                l1 = l1.next
            chain = chain.next
            
        while l1:
            chain.next = l1
            l1 = l1.next
            chain = chain.next
        while l2:
            chain.next = l2
            l2 = l2.next
            chain = chain.next

        return top.next