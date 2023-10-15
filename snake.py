from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

SNAKE_COLOR = "aqua"
colors = ["Pink", "PaleVioletRed", "HotPink", "DeepPink", "MediumVioletRed"]
#colors = ["Red", "Orange", "Yellow", "Lime", "Cyan", "Blue", "Indigo"]
COLOR_PALETTE = colors + colors[-2:0:-1]
NUMBER_OF_COLORS = len(COLOR_PALETTE)


class Snake:

    def __init__(self):

        self.body = []

        for i in range(3):
            self.add_body_segment()
            self.body[i].setx(-20 * i)


    def add_body_segment(self):
        new_seg = Turtle()
        self.body.append(new_seg)
        new_seg.shape("square")
        body_len = len(self.body)
        new_seg.color(COLOR_PALETTE[body_len % NUMBER_OF_COLORS])
        new_seg.penup()

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].goto(self.body[i - 1].pos())
        self.body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.body[0].heading() != DOWN:
            self.body[0].setheading(UP)

    def down(self):
        if self.body[0].heading() != UP:
            self.body[0].setheading(DOWN)

    def left(self):
        if self.body[0].heading() != RIGHT:
            self.body[0].setheading(LEFT)

    def right(self):
        if self.body[0].heading() != LEFT:
            self.body[0].setheading(RIGHT)

    def extend(self):
        self.add_body_segment()
        self.body[-1].goto(self.body[-2].pos())

    def reset(self):
        for segment in self.body:
            segment.hideturtle()
            segment.clear()
        self.body = []
        for i in range(3):
            self.add_body_segment()
            self.body[i].setx(-20 * i)
