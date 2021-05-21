# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:27:20 2021

@author: Mac_1
"""

import turtle as t
t.shape("turtle")
t.write("삼각형, 사각형, 원, 끝 중에 입력하세요.")



while True:
    s = t.textinput("input","도형을 입력하시오 : ")
    if s == "사각형":
        s = t.textinput("","가로길이")
        w = int(s)
        s = t.textinput("","세로길이")
        h = int(s)
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        t.forward(w)
        t.left(90)
        t.forward(h)
        
    elif s == "삼각형":
        s = t.textinput("","밑변의 길이를 입력하세요. ")
        w = int(s)
        t.forward(w)
        t.left(120)
        t.forward(w)
        t.left(120)
        t.forward(w)

    elif s == "원":
        s = t.textinput("","원의 반지름을 입력하세요. ")
        l = int(s)
        t.circle(l)
        
    elif s == "끝":
        break
    
    else:
        t.clear()
        t.goto(0,0)
    
    
t.exitonclick()