#Cohen-Sutherland line clipping algortihm
import turtle as t
t.speed=1
inside = 0  #0000
left = 1    #0001
right = 2   #0010
bottom = 4  #0100
top = 8     #1000

#Defining x_max,y_max and x_min,y_min for rectangle
X_max = 100.0
Y_max = 80.0
X_min = 40.0
Y_min = 40.0

def point(X_min,Y_min,X_max,Y_max):
    t.ht()
    t.up()
    t.goto(X_min,Y_min)
    t.down()
    t.goto(X_min,Y_max)
    t.goto(X_max,Y_max)
    t.goto(X_max,Y_min)
    t.goto(X_min,Y_min)

def draw(X1,Y1,X2,Y2):
    t.up()
    t.goto(X1,Y1)
    t.down()
    t.goto(X2,Y2)
    
# Function to compute region code for a point(x,y)
def compute(X,Y):
    code = inside
    if X < X_min:
        code = code or left
    elif X > X_max:
        code = code or right
    elif Y < Y_min:
        code = code or bottom
    elif Y > Y_max:
        code = code or top
    return code

def cohensutherlandclip(X1,Y1,X2,Y2):
    # Compute region codes for P1, P2 
    code1 = compute(X1,Y1)
    code2 = compute(X2,Y2)
    accept = False
    while True:
        # If both endpoints lie within rectangle 
        if code1 == 0 and code2 == 0:
            accept = True
            break
        # If both endpoints are outside rectangle 
        elif (code1 and code2) != 0:
            break
        # Some segment lies within the rectangle 
        else:

            # Line Needs clipping 
            # At least one of the points is outside,  
            # select it 
            X = 1.0
            Y = 1.0
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2
                 # Find intersection point using slope
                #m=(Y2-Y1)/(X2-X1)
            if code_out and top:
                 # point is above the clip rectangle 
               X = X1 + (X2 - X1) * (Y_max - Y1)/(Y2 - Y1)
               Y = Y_max
               
            elif code_out and bottom:
                 # point is below the clip rectangle 
                X=X1+(X2-X1)*(Y_min-Y1)/(Y2-Y1)
                Y=Y_min
                
            elif code_out and right:
                 # point is to the right of the clip rectangle 
                Y=Y1+(Y2-Y1)*(X_max-X1)/(X2-X1)
                X=X_max
                
            elif code_out and left:
                  # point is to the left of the clip rectangle 
                Y=Y1+(Y2-Y1)*(X_min-X1)/(X2-X1)
                X=X_min

                 # Now intersection point X,Y is found 
            # We replace point outside clipping rectangle 
            # by intersection point
            if code_out==code1:
                X1=X
                Y1=Y
                code1=compute(X1,Y1)
            else:
                X2=X
                Y2=Y
                code2=compute(X2,Y2)
    if accept:
        print("The line is accepted from %.2f,%.2f to %.2f,%.2f"%(X1,Y1,X2,Y2))
    else:
        print("Line Rejected from %.2f,%.2f to %.2f,%.2f"%(X1,Y1,X2,Y2))
    draw(X1,Y1,X2,Y2)
    
point(X_min,Y_min,X_max,Y_max)
cohensutherlandclip(50,50,80,70)
cohensutherlandclip(40,90,60,40)
cohensutherlandclip(10,50,40,10)