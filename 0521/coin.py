# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:52:55 2021

@author: Mac_1
"""

import turtle as t
import random

screen = t.Screen()
image1 = "d://front.gif"
image2 = "d://back.gif"
screen.addshape(image1)
screen.addshape(image2)

t1 = t.Turtle()
while True:
    t.delay(1000)
    coin = random.randint(0,1)
    if coin == 0:
        t1.shape(image1)
        t1.stamp()
    else: 
        t1.shape(image2)
        t1.stamp()
    
t.exitonclick()
