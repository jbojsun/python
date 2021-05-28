# -*- coding: utf-8 -*-
"""
Created on Fri May 28 14:32:15 2021
n_polygon.py
@author: Mac_1
"""

import turtle as t

def polygon(n,length):
    for i in range(n):
        t.forward(length)
        t.left(360//n)
        
for i in range(10):
    t.left(20)
    polygon(6,100)
    
t.done()
t.bye()