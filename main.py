import turtle as t
from tkinter import *
import random as r
from win32api import GetSystemMetrics as sm
h = sm(1)
w = sm(0)
t.colormode(255)    
def abstractart(x,y,z):
    rgb = (r.randint(0,255),r.randint(0,255),r.randint(0,255))
    t.pencolor(rgb)
    t.pencolor(rgb)
    t.pensize(x)
    t.forward(y)
    dran = r.random()
    if dran < 0.5:
        t.left(z)
    else:
        t.right(z)

    if t.xcor() < -300 or t.xcor() > 300:
        t.goto(r.randint(-300,300), r.randint(-300,300))
    elif t.ycor() < -300 or t.ycor() > 300:
        t.goto(0, 0)

def ranvals():
    x = r.randint(2,12)
    y = r.randint(0,100)
    z = r.randint(0,180)
    return x,y,z

for i in range(2000):
    x,y,z = ranvals()
    abstractart(x,y,z)
ts = t.getscreen()
ts.getcanvas().postscript(file="absart.eps")
