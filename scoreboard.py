from turtle import Turtle

ALIGN = "center"
FONT = ("Arial Black", 12, "bold")
with open("data.txt", mode="r") as file:
    HS = file.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = int(HS)
        self.penup()
        self.goto(0, 295)
        self.color("white")
        self.speed("fastest")
        self.hideturtle()
        self.score = 0
        self.prompt = ""
        self.refresh_prompt()

    def refresh_prompt(self):
        self.clear()
        self.prompt = f"Score: {self.score} HIGH SCORE: {self.high_score}"
        self.write(self.prompt, align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.refresh_prompt()

    def increase_score(self):
        self.score += 1
        self.refresh_prompt()
