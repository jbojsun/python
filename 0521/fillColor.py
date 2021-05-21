# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:11:32 2021

@author: Mac_1
"""

import turtle as t
t.shape('turtle')
colorList=["yellow","red","blue","green"]


for i in range(4):
    t.fillcolor(colorList[i])
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.penup()
    t.forward(50)
    t.pendown()
    
t.exitonclick()