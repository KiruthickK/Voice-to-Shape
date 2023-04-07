# Python program to demonstrate
# circle drawing  
import turtle
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
def Rectangle():
    # tod
    BendingWorks()

