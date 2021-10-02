#Program to implement the bouncing ball inside a defined rectangular Window.
import turtle
root = turtle.Screen()
root.bgcolor('black')
root.title('Bouncing Ball')

ball = turtle.Turtle()
ball.shape('circle')
ball.shapesize(2, 2)
ball.color('red')
ball.penup()
ball.speed(-5)
ball.goto(0, 200)
ball.dy = 0
ball.dx = 2
gravity = 0.1

while True:
    ball.dy -= gravity
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)
    if ball.xcor() > 300:
        ball.dx *= -1
    if ball.xcor() < -300:
        ball.dx *= -1
    if ball.ycor() < -300:
        ball.dy *= -1
