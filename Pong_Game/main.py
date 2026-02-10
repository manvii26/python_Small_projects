"""
main.py

This file is the main entry point of the Pong game.
It initializes the game screen, creates paddle, ball,
and scoreboard objects, handles keyboard input,
runs the game loop, and manages collisions and scoring.
"""


from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball((0,0))
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        ball.speed(3)

    #paddle
    if ball.distance(r_paddle) < 50 and ball.xcor()> 320 or ball.distance(l_paddle) < 50 and ball.xcor()< -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.resetpos()
        scoreboard.lpoint()

    if ball.xcor() < -380:
        ball.resetpos()
        scoreboard.rpoint()

screen.exitonclick()
