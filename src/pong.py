from turtle import *

# initlize the screen
screen = Screen()
screen.bgcolor("black")
screen.title("Ping Pong")
screen.setworldcoordinates(-500, -400, 500, 400)

# set ball and its position
ball = Turtle(shape="circle", visible=True)
ball.goto(0, 0)
ball.speed(0)
ball.color("green")
ball.penup()

# paddle
paddle = Turtle(shape="square", visible=True)
paddle.goto(0, -400)
paddle.speed(0)
paddle.resizemode("user")
paddle.shapesize(stretch_len=10, stretch_wid=1)
paddle.color("red")

# pen
pen = Turtle(shape="circle", visible=False)
pen.goto(-500, 380)
pen.color("white")

ballspeedx = 20
ballspeedy = 20
paddlespeed = 100
points = 0
gravity = -3
ballcompression = 1

def moveleft():
    paddle.setx(paddle.xcor() - paddlespeed)

def moveright():
    paddle.setx(paddle.xcor() + paddlespeed)

onkey(moveleft, "a")
onkey(moveright, "d")
listen()

while True:
    ball.setx(ball.xcor() + ballspeedx)
    ball.sety(ball.ycor() + ballspeedy)

    if ball.xcor() > 500 or ball.xcor() < -500:
        ballspeedx = ballspeedx * (-1) - ballcompression
    
    if ball.ycor() < -400:
        ballspeedy = (ballspeedy * (-1)) - ballcompression
    
    if ball.ycor() > 400:
        ballspeedy = ballspeedy * (-1) - ballcompression
    
    ball.sety(ball.ycor() + gravity)