# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:29:18 2021
triRect.py
@author: Mac_1
"""

import turtle as t

for i in range(3):
    t.forward(100)
    t.left(360/3)
    
t.penup()
t.goto(200,0)
t.pendown()

for i in range(4):
    t.forward(100)
    t.left(360/4)
    
    
t.done()