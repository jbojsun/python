# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:40:07 2021

@author: Mac_1
"""

import turtle as t

s=t.textinput("input","몇각형을 기다리겠습니까?")
n=int(s)

for i in range(n):
    t.forward(20)
    t.left(360/n)
    
t.done()