from turtle import Turtle

class Score(Turtle):
    def __init__(self, name):
        super().__init__()
        self.score = 0
        self.live = 5
        self.name = name
        self.write_score()


    def write_score(self):
        self.clear()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-550, 280)
        self.write(arg=f"SCORE: {self.score}", font=("courier", 12, "bold"), align="center")
        self.goto(0, 280)
        self.write(arg=self.name, font=("courier", 12, "bold"), align="center")
        self.goto(550,280)
        self.write(arg=f"🧡: {self.live}", font=("courier", 12, "bold"), align="center")

    def increase(self):
        self.score += 1
        self.write_score()

    def decrease_live(self):
        self.live -= 1
        self.write_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"*** Game Over ***\n Your final score: {self.score}",
                    font=("courier", 24, "bold"), align="center")