import turtle
import math

screen = turtle.Screen()
screen.bgcolor("Black")

t = turtle.Turtle()
t.shape("turtle")
t.color("black")
t.speed(3)

#Define a funcyion to draw and fill a rectangle with the given dimensions and color
def drawRectangle(t, width, height, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

#Define a funcyion to draw and fill a triangle with length and color.
#This is used to create a roof shape
def drawTriangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(length)
    t.left(135)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(135)
    t.end_fill()

#Draw and fill the front of the house
t.penup()
t.goto(0, -70)
t.pendown()
drawRectangle(t, 110,110, "pink")

#Draw and fill the front door
t.penup()
t.goto(50, -70)
t.pendown()
drawRectangle(t, 50, 60, "yellow")

#Front roof
t.penup()
t.goto(0, 40)
t.pendown()
drawTriangle(t, 150, "yellow")
#circle or window inside it
t.pu()
t.color("black")
t.goto(73,55)
t.pendown()
t.color('pink')
t.begin_fill()
t.circle(15)
t.penup()
t.end_fill()
t.penup()

#Bring turtle to front door
t.penup()
t.color("black")
t.goto(30, -80)
t.left(90)

#draw sun
def drawSun():
    t.color("Yellow")
    t.penup()
    t.goto(270, 220)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.penup()
    t.end_fill()
    t.penup()
    t.goto(220, 220)
    for i in range(8):
        t.pd()
        t.pensize(5)
        t.fd(100)
        t.bk(100)
        t.lt(45)
        t.penup()
        
drawSun()
screen.bgcolor("lightblue")       
t.color("black")
#To draw tree
def tree():
    t.goto(-80, 30)
    t.pd()
    t.color('green')
    t.begin_fill()
    t.lt(45)
    t.fd(200)
    t.lt(90)
    t.fd(200)
    t.lt(45)
    t.lt(90)
    t.fd(200)
    t.end_fill()
    t.pu()

tree()    
#To draw tree branch
t.color("black")
def branch():    
    t.goto(-265, 28)
    t.pd()
    t.color('brown')
    t.begin_fill()
    t.lt(180)
    t.lt(90)
    t.fd(90)
    t.lt(90)
    t.fd(90)
    t.lt(90)
    t.fd(90)
    t.end_fill()
    t.pu()
    t.ht()
    t.goto(0, 0)
       
branch()   