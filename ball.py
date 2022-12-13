import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.shapesize(1, 1)
        # self.goto(0, -280)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.05


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # def increase_speed(self):
    #     self.x_move *= 1.1
    #     self.y_move *= 1.1

    def bounce_x(self):
        self.x_move *= -1
        # self.move_speed *= 0.9

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.move_speed = 0.05
        self.goto(0, -280)
        self.bounce_y()