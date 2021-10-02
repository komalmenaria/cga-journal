import turtle
t = turtle.Turtle()
s = turtle.Screen()
a = 0
b = 0
x = 0
y = 50
M = (5/4)-y
while x <= y:
  if (M<0):
    M = M + 2 * x + 3
    yinc = y


  else:
    M = M + 2 * (x - y) + 5
    yinc = y - 1

  xinc = x + 1
  x = xinc + a
  y = yinc + b
  t.pu()
  t.goto(x, y)
  t.pd()
  t.begin_fill()
  t.color("red")
  t.goto(y,x)
  t.goto(y, -x)
  t.goto(x, -y)
  t.goto(-x, -y)
  t.goto(-y, -x)
  t.goto(-y, x)
  t.goto(-x,y)
  t.end_fill()
turtle.mainloop()