import random
from turtle import Turtle

COLORS= ["blue", "red", "yellow", "orange", "green", "indigo", "chartreuse"]

class Barriers:
    def __init__(self):
        self.all_barriers= []
        self.create_barriers()

    def create_barriers(self):
        ycor =280
        #set number of Rows
        for _ in range(5):
            xcor = -550
            #set number of column
            for _ in range(10):
                barrier= Turtle()
                barrier.shape("square")
                barrier.color(random.choice(COLORS))
                barrier.shapesize(stretch_wid=1, stretch_len=6)
                barrier.penup()
                barrier.goto(xcor, ycor)
                self.all_barriers.append(barrier)
                xcor += 122
            ycor -= 22