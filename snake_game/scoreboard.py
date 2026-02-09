"""
scoreboard.py

This file defines the Scoreboard class.
It manages score display, updates during gameplay,
and shows the game-over message when the game ends.
"""



from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.up_score()

    def up_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align="center", font=("Courier", 24, "bold"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.up_score()
