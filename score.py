from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.live = 5
        self.write_score()


    def write_score(self):
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-550, 280)
        self.write(arg=f"SCORE: {self.score}", font=("courier", 12, "bold"), align="center")
        self.goto(550,280)
        self.write(arg=f"🧡: {self.live}", font=("courier", 12, "bold"), align="center")

    # def write_live