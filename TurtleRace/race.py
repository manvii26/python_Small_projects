"""
race.py

A simple Turtle Race game where the user places a bet on a turtle color.
Each turtle moves forward by a random distance until one reaches the finish line.

Concepts used:
- Python turtle module
- Loops and conditionals
- Random module
- Basic user interaction
"""


from turtle import Turtle, Screen
import random
import time

screen = Screen()
is_race = "false"
screen.setup(width=500, height=600)
user_bet = screen.textinput(title ="Make your bet", prompt="Which turtle will win the race? Why don't you enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions =[100,70,40,10,-20,-50]

our_turtles = []


for turtle_index in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[turtle_index])
    our_turtles.append(new_turtle)


if user_bet:
    is_race = True

while is_race:


    for turtle in our_turtles:
        if turtle.xcor() > 215:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!!")
            else:
                print(f"You loose! The {winning_color} turtle is the winner!!")
            time.sleep(4)
            screen.bye()
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()
