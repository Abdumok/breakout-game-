from turtle import Screen
from paddle import Paddle

#Setup Main Screen:
window= Screen()
window.title("Breakout Game v1.00")
window.bgcolor("black")
window.setup(width=1200, height=600)

paddle= Paddle()



window.exitonclick()