from turtle import *

# initlize the screen
screen = Screen()
screen.bgcolor("black")
screen.title("Ping Pong")
screen.setworldcoordinates(-500, -400, 500, 400)

# set ball and its position
ball = Turtle(shape="circle", visible=True)
ball.goto(0, 0)
ball.speed(10)
ball.color("green")
ball.penup()

# paddle
paddle = Turtle(shape="square", visible=True)
paddle.goto(0, -400)
paddle.speed("normal")
paddle.resizemode("user")
paddle.shapesize(stretch_len=10, stretch_wid=1)
paddle.color("red")

points = 0
ballspeedx = 5
ballspeedy = 5
paddlespeed = 2

while True:
    if points == 10:
        break
    # change balls position
    ball.setx(ball.xcor() + ballspeedx)
    ball.sety(ball.ycor() + ballspeedy)

    # check if ball is at the edge of the screen
    if ball.xcor() >= 500 or ball.xcor() <= -500:
        ballspeedx = ballspeedx * (-1)

    if ball.ycor() >= 400 or ball.ycor() <= -400:
        ballspeedy = ballspeedy * (-1)

done()