import turtle
line = turtle.Turtle()
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
e = (dy/dx) - 0.5
x = x1
y = y1
line.pu()
for i in range(dx + 1):
    print("x : ",(round(x)), "y : ",(round(y)))
    line.goto(x * 10, y * 10)
    line.pd()
    while e>=0:
      y = y + 1
      e = e - 1
    x = x + 1
    e = (dy/dx) + e
turtle.mainloop()