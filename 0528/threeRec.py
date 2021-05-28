# -*- coding: utf-8 -*-
"""
Created on Fri May 28 14:24:13 2021
threeRec.py
@author: Mac_1
"""

import turtle as t
t.shape("turtle")

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)
        
i=0
for i in range(-200,400,200): #range(start, end, 간격)
    t.up()
    t.goto(i,0)
    t.down()
    square(100)

t.done()
t.bye()