from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.penup()
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.rand_x = random.randint(-280, 280)
        self.rand_y = random.randint(-280, 280)
        self.goto(self.rand_x, self.rand_y)
