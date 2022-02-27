from turtle import *

# initlize the screen
screen = Screen()
screen.bgcolor("yellow")
screen.title("Ping Pong")
screen.setworldcoordinates(-500, -400, 500, 400)

# set ball and its position
ball = Turtle(shape="circle", visible=True)
ball.penup()
ball.goto(0, 0)
ball.speed(0)
ball.color("green")

# paddle
paddle = Turtle(shape="square", visible=True)
paddle.penup()
paddle.goto(0, -400)
paddle.speed(0)
paddle.resizemode("user")
paddle.shapesize(stretch_len=10, stretch_wid=1)
paddle.color("red")

# pen
pen = Turtle(shape="circle", visible=False)
pen.penup()
pen.goto(-500, 380)
pen.color("black")
pen.pendown()

ballspeedy = 20
ballspeedx = -30
paddlespeed = 100
points = 0
gravity = -8
ballcompression = 5
px = 20
py = 20

# display points
pen.write(f"Points {points}", font=("Consolas", 20, "bold"))

def moveleft():
    paddle.setx(paddle.xcor() - paddlespeed)

def moveright():
    paddle.setx(paddle.xcor() + paddlespeed)

onkey(moveleft, "a")
onkey(moveright, "d")
listen()

while True:
    # move ball
    ball.setx(ball.xcor() + ballspeedx)
    ball.sety(ball.ycor() + ballspeedy)

    # check if coliding with paddle
    if (ball.xcor() < paddle.xcor() + 190.00 and ball.xcor() > paddle.xcor() - 170.00) and (ball.ycor() > -420 and ball.ycor() < -380):
        ball.setx(ball.xcor() + px)
        ball.sety(ball.ycor() + py)
        # increase paddle force for next hit
        py = py + 10
        if px < 0:
            px = px - 20
        else:
            px = px + 20
        px = px * (-1)
        ballspeedx = px
        ballspeedy = py
        # update points
        points += 1
        # display results
        pen.clear()
        pen.write(f"Points {points}", font=("Consolas", 20, "bold"))

    # check if ball at edge
    if ball.xcor() > 500:
        ball.setx(500)
        ballspeedx = ballspeedx * (-1)
        if ballspeedx < 0:
            ballspeedx = ballspeedx + ballcompression
        else:
            ballspeedx = ballspeedx - ballcompression
    
    if ball.xcor() < -500:
        ball.setx(-500)
        ballspeedx = ballspeedx * (-1)
        if ballspeedx < 0:
            ballspeedx = ballspeedx + ballcompression
        else:
            ballspeedx = ballspeedx - ballcompression
    
    if ball.ycor() < -400:
        ball.sety(-400)
        ballspeedy = ballspeedy * (-1)
        # decrease paddle force for next hit
        if ballspeedy < 0:
            ballspeedy = ballspeedy + ballcompression
        else:
            ballspeedy = ballspeedy - ballcompression
        px = 20
        py = 20
        # update points
        points = points - 1
        # display results
        pen.clear()
        pen.write(f"Points {points}", font=("Consolas", 20, "bold"))
    
    if ball.ycor() > 400:
        ball.sety(400)
        ballspeedy = ballspeedy * (-1)
        if ballspeedy < 0:
            ballspeedy = ballspeedy + ballcompression
        else:
            ballspeedy = ballspeedy - ballcompression
    
    ball.sety(ball.ycor() + gravity)