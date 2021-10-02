#scaling in 2D Homogeneous coordinates
import turtle 
import numpy as np

ka = turtle.Turtle()
ka.setposition(0,0)
ka.pd() 
ka.pu() 
ka.setposition(30,60) 
ka.pd() 
ka.write("original object") 
x = np.array([[0,0, 1], [40,50, 1], [0,0,1]]) 
y = np.array([[3,0,0], [0,4,0],[0,0,1]]) 
result = np.array([[0,0,0], [0,0,0],[0,0,0]]) 

result = x.dot(y)
for r in result:
    print(r) 
def Scaling(result): 
    ka.pu() 
    ka.setposition(0,0)
    ka.pd()
    for point in result: 
        ka.goto(point[0], point[1])

Scaling(result) 
ka.pu() 
ka.setposition(60,20) 
ka.pd() 
ka.write("scale object") 
turtle.mainloop()
