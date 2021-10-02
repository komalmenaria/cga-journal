#2d rotation with homogeneous coordinates 
import turtle as tur
import numpy as np 
t = tur.Turtle() 
t.speed(4) 
t.goto(75,75)
t.pu() 
t.goto(20,-40) 
t.pd()
t.write("original object")
x = np.array([[0,0,1],[75,75,1],[0,0,1]])
y = np.array([[0,0,0],[-1,1,0],[0,0,1]])
result = np.array([[0,0,0],[0,0,0],[0,0,0]])
result = x.dot(y) 

for r in result:
   print(r)

t.pu()
t.goto(0,0)
t.down()
def rotate(result): 
    t.setposition(0,0) 
    t.pd()
    for point in result: 
        t.goto(point[0], point[1])


rotate(result) 
t.goto(0,0)
t.pu()
t.goto(-90,-40) 
t.pd()
t.write("Rotated object")  
t.hideturtle() 
tur.mainloop() 