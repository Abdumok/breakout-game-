from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_step = 3
        self.y_step = 3

    def move(self):
        self.goto(self.xcor() - self.x_step, self.ycor() - self.y_step)

    def bounce(self):
        self.y_step *= -1

    def bounce_from_wall(self):
        self.x_step *= -1

