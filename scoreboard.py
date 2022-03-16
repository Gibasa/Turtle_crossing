from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.reach_end()

    def game_over(self):
        self.goto(-100, 0)
        self.write(f"GAME OVER", align="left", font=FONT)

    def reach_end(self):
        self.clear()
        self.score += 1
        self.goto(-280, 230)
        self.write(f"Level:{self.score}", align="left", font=FONT)

