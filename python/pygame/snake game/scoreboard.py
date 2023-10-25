from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        with open("P:/python projects/turtle GUI/snake game/data.txt") as file:
           self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_highscore(self):
        with open("P:/python projects/turtle GUI/snake game/data.txt", mode="w") as file:
            file.write(f"{self.highscore}")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
            self.update_highscore()
        self.update_scoreboard()
