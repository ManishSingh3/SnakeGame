from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Verdana", 11, "normal")

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 230)
        self.count = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score:{self.count}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)
    def count_score(self):
        self.count += 1
        self.clear()
        self.update_score()


    