import time
from turtle import Screen
from paddle import Paddle
from barriers import Barriers
from ball import Ball
from score import Score
#Setup Main Screen:
window= Screen()
window.title("Breakout Game v1.00")
window.bgcolor("black")
window.setup(width=1200, height=600)
window.tracer(0)

# Ask the player for his name:
player_name = window.textinput(title="Player Name", prompt="Enter your name:")

paddle= Paddle()
# control paddle movement:
window.listen()
window.onkey(fun=paddle.go_left, key="Left")
window.onkey(fun=paddle.go_right, key="Right")


barriers= Barriers()
ball= Ball()
score= Score(name=player_name)


game_on = True
while game_on:
    ball.move()
    # Detect the collision with paddle:
    for part in paddle.all_parts:
        if part.distance(ball) < 20:
            ball.bounce()
    # Detect the collision with wall
    if ball.xcor() < -590 or ball.xcor() > 590:
        ball.bounce_from_wall()
    # Detect the collision with top wall:
    if ball.ycor() > 280:
        ball.bounce()
    # Detect the collision with barriers
    for barrier in barriers.all_barriers:
        if ball.distance(barrier) < 50:
            ball.bounce()
            barrier.goto(1000,1000)
            barriers.all_barriers.remove(barrier)
            score.increase()
            if barriers.all_barriers == 0:
                window.bgcolor("green")
                score.winning()
                game_on = False
    # IF paddle miss the ball:
    if ball.ycor() < -350:
        score.decrease_live()
        if score.live == 0:
            score.game_over()
            ball.clear()
            window.bgcolor("red")
            game_on = False
        ball.recenter()
    window.update()
window.exitonclick()