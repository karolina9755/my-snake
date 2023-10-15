import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

WALL_POSITION = 290

screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # 0 - off

snake = Snake()
food = Food()
scoreboard = Scoreboard()


# f = Food()
# f.color("magenta")
# f.goto(WALL_POSITION-10,WALL_POSITION-10)


def draw_wall():
    wall = Turtle()
    wall.hideturtle()
    wall.color("white")
    wall.penup()
    wall.goto(-WALL_POSITION, -WALL_POSITION)
    wall.setheading(90)
    wall.pendown()
    while wall.ycor() < WALL_POSITION:
        wall.forward(1)
    wall.right(90)
    while wall.xcor() < WALL_POSITION:
        wall.forward(1)
    wall.right(90)
    while wall.ycor() > -WALL_POSITION:
        wall.forward(1)
    wall.right(90)
    while wall.xcor() > -WALL_POSITION:
        wall.forward(1)
    wall.penup()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
draw_wall()

while game_on:
    screen.update()
    time.sleep(0.08)

    snake.move()

    # snake eats food
    if snake.body[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # snake collides with its tail
    for segment in snake.body[1:]:
        if snake.body[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            print("Snake hit its tail.")

    # snake collides with a wall
    if abs(snake.body[0].xcor()) > WALL_POSITION or abs(snake.body[0].ycor()) > WALL_POSITION:
        scoreboard.reset()
        snake.reset()
        print("Snake hit the wall.")

screen.exitonclick()
