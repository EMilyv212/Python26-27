import turtle
from random import *
bob = turtle.Turtle()
turtle.colormode(255)
turtle.bgcolor("black")
turtle.tracer(0)

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def one(size, width):
    bob.setheading(0)
    bob.width(width)
    bob.left(90)
    bob.forward(size)
    bob.left(125)
    bob.forward(size/2)

def zero(size, width):
    bob.setheading(135)
    bob.width(width)
    for times in range(2):
        bob.circle(size,90)
        bob.circle(size+10,90)
        
def rectangle(size1, size2, width):
    bob.setheading(0)
    bob.width(width)
    for times in range(2):
        bob.forward(size1)
        bob.left(90)
        bob.forward(size2)
        bob.left(90)

def diamond(size1, size2, width):
    bob.width(width)
    for times in range(2):
        bob.forward(size1)
        bob.left(90)
        bob.forward(size2)
        bob.left(90)
