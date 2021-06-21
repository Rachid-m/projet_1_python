#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 17:56:37 2021

@author: papasambadia
"""

from DessinMSDA import *
from turtle import *
from math import *
from random import *
width(5)
up()
goto(-40,0)
down()
colors=["cyan","purple","white","blue","yellow","black"]
color(choice(colors))

begin_fill()  #Précise le début du remplissage
right(56)
rectangle(30,272)
end_fill()
fd(26)
left(90)
up()
fd(253)
down()
right(38)
begin_fill()
elipse(24)
end_fill()
begin_fill()
up()
goto(-40,0)
down()
left(170)
fd(46)
left(70)
fd(35)
right(70)
backward(45)
left(100)
fd(45)
left(99)
fd(36)
left(77)
fd(50)
right(48)
up()
fd(116)
down()
right(120)
fd(135)
left(110)
fd(35)
left(60)
fd(160)
left(133)
fd(70)
right(90)
up()
fd(32)
down()
left(40)
fd(135)
right(110)
fd(35)
right(64)
fd(166)
end_fill()
up()
left(40)
fd(180)
down()

mainloop()

