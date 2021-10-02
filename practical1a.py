import turtle
s = turtle.getscreen()
t=turtle.Turtle()
turtle.bgcolor("blue")
t.pensize(width=3)
t.pencolor("red")
t.shape("turtle")
t.fillcolor("yellow")
t.speed(1)

def draw(s):
    for i in range(4):
        t.fd(s)
        t.pu()
        t.goto(0,0)
        t.pd()
        t.lt(90)

draw(300)