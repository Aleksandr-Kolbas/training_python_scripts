#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 23:13:34 2019

@author: aleksandr
"""

'''You should choose a text-file and input its name in function 'open'. 
If text-file doesn't place in the same directiry as the python-file, 
you need to input path for the text-file before its name.'''

with open('test.txt', 'r') as inf:  
    txt = inf.read().strip().lower().split()      
    txt.sort()                                    
entr = {}                                         
for i in txt:
    #add in dict words like keys & numbers of their repetitions like values     
    entr[i] = txt.count(i)         
print(max(entr, key = entr.get), max(entr.values()))
