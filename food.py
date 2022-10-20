from turtle import Turtle
import random

WALL_POSITION = 290

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("gold")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-WALL_POSITION+10, WALL_POSITION-10)
        random_y = random.randint(-WALL_POSITION+10, WALL_POSITION-10)
        self.goto(random_x, random_y)
