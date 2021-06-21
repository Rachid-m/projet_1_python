#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 17:42:06 2021

@author: papasambadia
"""

from turtle import *
from math import *
def cercle(rayon):
    circle(rayon)
def demi_cercle(rayon):
    circle(rayon,180)
def triangle(x):
     
    for i in range(3):
        forward(x)
        left(120)
 


def carre(x):
     
    for i in range(4):
        fd(x)
        left(90)

 

def rectangle(x,y):
    for i in range(2):
        fd(x)
        left(90)
        fd(y)
        left(90)
        
        
def polygone(x):
    for i in range(x):
        forward(100)
        left(360/x)
def trapeze(x,y,z):
    left(180)
    fd(x)
    left(90)
    fd(y)
    left(90)
    fd(z)
    goto(0,0)

def elipse(rayon):
    for i in range(2):
	# two arcs
	    circle(rayon,90)
	    circle(rayon//2,90)
def Init(pen,px,py):
  
  pen.up()
  pen.goto(px,py)
  pen.down()
 

#
def DrawRect(x,y,longueur,largeur):
  pen=Turtle()
  pen.speed(50)
  pen.color("gold")
  pen.begin_fill()
  pen.pensize(5)
  Init(pen,x,y)
  for i in range(0,2):
    pen.fd(longueur)
    pen.left(90)
    pen.fd(largeur)
    pen.left(90)
    pen.hideturtle()
  pen.end_fill()
#
#
def DrawTube(x,y,longueur,largeur):
  
  pen=Turtle()
  pen.speed(50)
  pen.color('white')
  pen.begin_fill()
  pen.pensize(5)
  Init(pen,x,y)
  pen.right(90)
  pen.circle(largeur/2,-180)
  pen.bk(longueur-(largeur/2))
  pen.left(90)
  pen.fd(largeur)
  pen.right(90)
  pen.fd(longueur-(largeur/2))
  pen.speed(25)
  pen.hideturtle()
  pen.end_fill()
  



#Cercle
def DrawRectSemiCircle(x,y,rayon):
  pen=Turtle()
  pen.speed(50)
  pen.color('green')
  pen.begin_fill()
  Init(pen,x,y)
  pen.pensize(5)
  pen.right(90)
  pen.circle(rayon,-180)
  pen.left(90)
  pen.fd(rayon*2)
  pen.hideturtle()
  pen.end_fill()


  

#poteau
def Poteau(x,y,largeur,longueur):
  pen=Turtle()
  pen.speed(50)
  pen.color('gold')
  pen.begin_fill()
  Init(pen,x,y)
  pen.pensize(5)
  pen.left(90)
  pen.fd(longueur)
  pen.right(90)
  pen.fd(largeur)
  pen.right(90)
  pen.fd(longueur)
  pen.right(90)
  pen.fd(largeur)
  pen.hideturtle()
  pen.end_fill()
#Motif
def Motif(x,y,largeur,longueur):
  pen=Turtle()
  
  pen.speed(50)
  Init(pen,x,y)
  pen.pensize(5)
  pen.left(90)
  pen.fd(longueur/8)
  Init(pen,x+(longueur/8),y+(longueur/4))
  pen.begin_fill()
  pen.circle(longueur/8)
  pen.end_fill()
  Init(pen,x,y+(3*longueur/8))
  pen.fd(longueur/8)
  Init(pen,x+(longueur/16),y+(9*longueur/16))
  pen.begin_fill()
  pen.circle(longueur/16)
  pen.end_fill()
  Init(pen,x,y+(5*longueur/8))
  pen.fd(3*longueur/8)
  