# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:40:02 2021

@author: Mac_1
"""

import turtle as t
t.shape('turtle')
t.shapesize(3)
t.width(3,3)


while True:
    command = t.textinput("명령을 입력하시오.")
    if command =="l":
        t.left(90)
        t.forward(100)
    if command =="r":
        t.right(90)
        t.forward(100)
