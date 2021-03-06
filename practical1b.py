import turtle

wn = turtle.Screen()#setup screen and its attributes
tess = turtle.Turtle() #set tess
tess.speed(2)

def draw_axis(s):
    #draws x,y axis
    tess.setpos(0,0)
    tess.shape("turtle")
    tess.color("black")
    tess.pensize(5)

    for i in range(4):
        tess.fd(s)
        tess.pu()
        tess.goto(0,0)
        tess.pd()
        tess.lt(90)
    tess.ht

draw_axis(300)

tess.penup()
tess.goto(-120,40)
tess.begin_fill()
tess.color("yellow")
tess.pendown()
tess.circle(50)
tess.penup()
tess.goto(-140,10)
tess.end_fill()
tess.pendown()
tess.write("circle")

tess.penup()
tess.setposition(120,100)
tess.pendown()
tess.begin_fill()
tess.color("blue")
tess.circle(40,200,10)
tess.end_fill()
tess.penup()
tess.setposition(180,110)
tess.pendown()
tess.write("half circle")

tess.penup()
tess.setposition(130,-150)
tess.pendown()
tess.begin_fill()
tess.color("magenta")
tess.forward(50)
tess.left(90)
tess.forward(100)
tess.left(90)
tess.forward(50)
tess.left(90)
tess.forward(100)
tess.left(90)
tess.end_fill()
tess.penup()
tess.setposition(140,-160)
tess.pendown()
tess.write("Rectangle")

tess.penup()
tess.setposition(-130,-150)
tess.pendown()
tess.begin_fill()
tess.color("red")
tess.forward(10)
tess.left(90)
tess.forward(100)
tess.left(135)
tess.forward(140)
tess.end_fill()
tess.penup()
tess.setposition(-100,-120)
tess.pendown()
tess.write("Triangle")
tess.penup()
tess.goto(0, 0)