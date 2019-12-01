from turtle import *
import turtle

def pos():
    penup()
    goto(-100,-180)
    pendown()
    left(90)

def border():
    forward(400)
    backward(400)
    right(90)
    forward(300)
    left(135)
    forward(300)
    right(135)
    forward(213)
    left(148)
    forward(355)
    left(122)
    forward(400)
    
def border1():
    right(90)
    penup()
    forward(16)
    pendown()
    right(90)
    forward(430)
    right(122)
    forward(435)
    right(148)
    forward(230)
    left(135)
    forward(308)
    right(135)
    forward(357)
    right(90)
    forward(30)
    
def moon():
    left(180)
    circle(60,180)
    left(140)
    circle(-130,12)
    right(70)
    forward(7)
    for i in range(8):
        right(100)
        forward(12)
        left(120)
        forward(12)
        
    right(105)
    forward(7)
    right(60)
    circle(-125,12)
    
def sun():
    for i in range(12):
        left(31.8)
        forward(18)
        left(85.2)
        forward(18)
        right(146.9)
    
pos()
color('blue','blue')
begin_fill()
border()
border1()
end_fill()
pos()
right(90)
color('blue','red')
begin_fill()
border()
end_fill()
backward(400)
left(238)
penup()
backward(15)
right(50)
backward(110)
right(8)
pendown()
color('white','white')
begin_fill()
moon()
end_fill()
left(140)
penup()
forward(175)
left(90)
forward(8)
pendown()
color('white','white')
begin_fill()
sun()
end_fill()
penup()
forward(20)
done()













