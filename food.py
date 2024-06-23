from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        # we only have access to shape, penup, and shapesize be cause we inherited from the Turtle class
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
