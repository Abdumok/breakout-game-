from turtle import Screen
from paddle import Paddle
from barriers import Barriers

#Setup Main Screen:
window= Screen()
window.title("Breakout Game v1.00")
window.bgcolor("black")
window.setup(width=1200, height=600)
window.tracer(0)

paddle= Paddle()
# control paddle movement:
window.listen()
window.onkey(fun=paddle.go_left, key="Left")
window.onkey(fun=paddle.go_right, key="Right")


barriers= Barriers()
game_on = True
while game_on:
    window.update()

window.exitonclick()