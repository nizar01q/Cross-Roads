from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("gainsboro")
        self.penup()
        self.hideturtle()
        self.goto(-200, 265)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 20)
        self.write("GAME OVER", align="center", font=("courier", 40, "normal"))

