from turtle import Screen
from paddle import Paddle
from ball import Ball
from blocks import Blocks
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Breakout Game")
screen.tracer(0)

player = Paddle()
ball = Ball()
blocks_list = []

# Creating Blocks
x = -350
y = 190
blocks_colors = ["Red", "Yellow", "Green", "White"]
for color in blocks_colors:
    x = -350
    y += 30
    for n in range(0, 11):
        blocks_list.append(Blocks(color, x, y))
        x += 70

screen.listen()
screen.onkey(player.move_right, "Right")
screen.onkey(player.move_left, "Left")
ball.setheading(170)
ball.goto(0, -280)
screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect wall collision
    if (ball.xcor() > 360) or (ball.xcor() < -360):
        ball.bounce_x()

    # detect paddle collision
    if (player.distance(ball) < 40) and (ball.ycor() < -300):
        ball.bounce_y()
    elif ball.ycor() > 360:
        ball.bounce_y()
    elif ball.ycor() < -380:
        ball.reset_position()

    # detect blocks collision
    for block in blocks_list:
        if block.distance(ball) < 40:
            ball.bounce_y()
            block.reset()
            blocks_list.remove(block)

screen.exitonclick()
