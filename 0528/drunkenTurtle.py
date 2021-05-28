# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:46:11 2021
drunkenTurtle.py
@author: Mac_1
"""

import turtle as t
import random

for i in range(30):
    length=random.randint(20, 100) 
    t.forward(length)
    angle=random.randint(0,360)
    t.left(angle)
    
t.done()
