"""
scoreboard.py

This file defines the Scoreboard class.
It tracks and displays player scores and
updates the score whenever a point is scored.
"""


from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.up_scoreboard()

    def up_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.lscore,align="center",font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.rscore,align="center",font=("Courier",80,"normal"))

    def lpoint(self):
        self.lscore += 1
        self.up_scoreboard()

    def rpoint(self):
        self.rscore += 1
        self.up_scoreboard()
