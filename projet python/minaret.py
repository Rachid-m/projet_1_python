#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 18:02:39 2021

@author: papasambadia
"""

from DessinMSDA import *
from turtle import *
from math import *
from random import *
width(3)
DrawRect(-300,-320,600,200)

DrawRect(-300,-320,600,60)
for i in range(7):
    DrawTube(-255+75*i,-170,119,60)
DrawRect(-250,-120,500,130)
for i in range(7):
    DrawTube(-200+60*i,-40,85,45)

DrawRectSemiCircle(-220,13,220)
Motif(0,237,100,100)
#minaret !
Poteau(260,-322,100,450)
up()
goto(260,130)
down()
color('green')
begin_fill()
triangle(100)
end_fill()
Motif(310,218,100,100)
#minaret 2
Poteau(-360,-322,100,450)
up()
goto(-360,130)
down()
color('green')
begin_fill()
triangle(100)
end_fill()
Motif(-310,218,100,100)
up()
goto(-425,-319)
down()
#width(15)
#fd(900)
DrawTube(283,90,105,50)
DrawTube(-333,90,105,50)
hideturtle()













mainloop()
