"""
main.py

This file is the entry point of the Snake Game.
It initializes the game window, handles user input,
controls the main game loop, and manages interactions
between the snake, food, and scoreboard.
"""


from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


gameOn = True

while gameOn:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Collison with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.add_score()

    #collison with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        gameOn = False
        scoreboard.game_over()

    #collison with self

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameOn = False
            scoreboard.game_over()









screen.exitonclick()
