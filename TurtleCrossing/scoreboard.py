from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.goto(-250, 250)
        self.write(arg=f"Level: {self.score}", align="left", font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.write(arg="Game Over", align="center", font=FONT)
