from turtle import Turtle
START_POS = [-50, -30, -10, 10, 30, 50]
class Paddle:
    def __init__(self):
        self.all_parts= []
        self.create_paddle()

    def create_paddle(self):
        for pos in START_POS:
            part = Turtle()
            part.penup()
            part.color("white")
            part.shape("square")
            part.goto(pos, -250)
            self.all_parts.append(part)

    def go_left(self):
        for part in self.all_parts:
            part.goto(part.xcor() -40, part.ycor())

    def go_right(self):
        for part in self.all_parts:
            part.goto(part.xcor() + 40, part.ycor())
