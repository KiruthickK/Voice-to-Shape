# Python program to demonstrate
# circle drawing  
import turtle
from turtle import *
import tkinter as tk
from PIL import Image, ImageDraw
import io
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
def SaveTurltle():
    # get the turtle window's canvas object
    canvas = turtle.getcanvas()

    # create a PostScript representation of the canvas
    postscript_data = canvas.postscript()

    # create an Image object from the PostScript data
    image = Image.open(io.BytesIO(postscript_data.encode('utf-8')))

    # save the image to a file
    image.save("turtle_image.png", "png")
# TangentCircle()
# Square()
# SaveTurltle()
# ChangeDirection("right")
# TangentCircle()



def IndianFlag():
# screen for output
    # screen = turtle.Screen()
    # Defining a turtle Instance
    speed(1)

    # initially penup()
    t.penup()
    t.goto(-200, 125)
    t.pendown()
    # Orange Rectangle
    #white rectangle
    t.color("orange")
    t.begin_fill()
    t.forward(400)
    t.right(90)
    t.forward(84)
    t.right(90)
    t.forward(400)
    t.end_fill()
    t.left(90)
    t.forward(84)

    # Green Rectangle
    t.color("green")
    t.begin_fill()
    t.forward(84)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(84)
    t.end_fill()

    # Big Blue Circle
    t.penup()
    t.goto(35, 0)
    t.pendown()
    t.color("navy")
    t.begin_fill()
    t.circle(35)
    t.end_fill()

    # Big White Circle
    t.penup()
    t.goto(30, 0)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    #Mini Blue Circles of Flag
    t.penup()
    t.goto(-27, -4)
    t.pendown()
    t.color("navy")
    for i in range(24):
        t.begin_fill()
        t.circle(2)
        t.end_fill()
        t.penup()
        t.forward(7)
        t.right(15)
        t.pendown()

    # Small Blue Circle
    t.color("navy")
    t.penup()
    t.goto(10, 0)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    #The spokes of India Flag
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.pensize(1)
    for i in range(24):
        t.forward(30)
        t.backward(30)
        t.left(15)

    #for stick of the flag
    t.color("Brown")
    t.pensize(10)
    t.penup()
    t.goto(-200,125)
    t.right(180)
    t.pendown()
    t.forward(800)
    t.home()
    #to hold the
    #output window
    # turtle.done()
