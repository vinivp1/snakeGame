from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align = "center", font = ("Arial", 15,"normal" ))

    def plus_point(self):
        self.score += 1

