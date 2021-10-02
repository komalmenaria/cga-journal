#2D reflection with homogeneous coordinates 
import turtle as t
import numpy as np
sq = t.Turtle() 
sq.speed = 1
for i in range(0,4): 
    sq.forward(100) 
    sq.left(90)
sq.up() 
sq.setposition(20,-40) 
sq.down()
sq.write("original object")


x = np.array([[0,0,1], [0,100,1], [100,100,1],[100,0,1]])
y = np.array([[-1,0,0],[0,-1,0],[0,0,1]])
result = np.array([[0,0,0], [0,0.0],[0,0,0],[0,0,0]])

result = x.dot(y) 
for r in result:
   print(r)
sq.up() 
sq.setposition(0,0) 
sq.down()


for point in result: 
    sq.goto(point[0], point[1])

sq.goto(0,0)
sq.up()
sq.setposition(-90,-40) 
sq.down() 
sq.write("reflection object") 
t.hideturtle()
t.mainloop()