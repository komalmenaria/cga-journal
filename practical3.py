import turtle
import math
screen = turtle.Screen()
screen.bgcolor("black")
line = turtle.Turtle()
line.shape("circle")
line.color("yellow")
line.pensize(width=6)
x1 = int(input("Enter x1 : "))
print(x1)
y1 = int(input("Enter y1 : "))
print(y1)
x2 = int(input("Enter x2 : "))
print(x2)
y2 = int(input("Enter y2 : "))
print(y2)
dx = x2 - x1
dy = y2 - y1
if (abs(dx) >= abs(dy)):
  step = abs(dx)
else:
  step = abs(dy)
xinc = dx/step
yinc = dy/step
xnew = x1 + 0.5 * math.asin(xinc)
ynew = y1 + 0.5 * math.asin(yinc)
line.pu()
i = 1
while(i <= step):
     print("x : ",(int(xnew)), "y : ",(int(ynew)))
     line.goto(xnew * 10, ynew * 10)
     line.pd()
     xnew = xnew + xinc
     ynew = ynew + yinc
     i = i +1
turtle.hideturtle()
turtle.mainloop()