from turtle import Turtle

ALIGN = "center"
FONT = ("Arial Black", 12, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 300)
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.score = 0
        self.prompt = ""
        self.refresh_prompt()

    def refresh_prompt(self):
        self.clear()
        self.prompt = f"Score: {self.score}"
        self.write(self.prompt, align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        #self.color("green")
        self.write("GAME OVER", align=ALIGN, font=("Arial Black", 16, "bold"))

    def increase_score(self):
        self.score += 1
        self.refresh_prompt()
