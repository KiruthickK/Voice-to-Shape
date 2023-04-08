# Python program to demonstrate
# circle drawing  
import turtle
from turtle import *
t = turtle.Turtle()
# Initializing the turtle
def BendingWorks():
    print("Bending works!")
def DrawCircle():
    r = 50
    t.circle(r)
def TangentCircle():
    r = 10
    # number of circles
    n = 10
    # loop for printing tangent circles
    for i in range(1, n + 1, 1):
        t.circle(r * i)
def ClearDrawings():
    t.clear()
    # clear()
def Square():
    # tod
    for i in range(4):
        t.forward(50)
        t.right(90)
def StraightLine(distance, direction):
    if(direction == "right"):
        t.right(90)
        t.forward(distance)
    if(direction == "left"):
        t.left(90)
        t.forward(distance)
    if(direction == "backward"):
        t.backward(90)
        t.forward(distance)
    if(direction == "forward"):
        t.forward(distance)

def TurtleStar():
    # t.color('red', 'yellow')
    # t.begin_fill()
    # i = 0
    for i in range(0,35):
        t.forward(200)
        t.left(170)
    # end_fill()
# TurtleStar()
def ChangeDirection(direction):
    if(direction == "right"):
        t.right(90)
    if(direction == "left"):
        t.left(90)
    if(direction == "backward"):
        t.backward(90)
    # if(direction == "forward"):
    #     t.forward(10)
# TangentCircle()
# ChangeDirection("right")
# TangentCircle()

