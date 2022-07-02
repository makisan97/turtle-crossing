from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 0
        with open("data.txt", mode="r") as data:
            self.highscore = int(data.read())
        self.penup()
        self.goto(-280, 250)
        self.color("black")
        self.update_level()

    def update_level(self):
        self.write(f"Level: {self.level}  HighScore: {self.highscore}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        if self.level > self.highscore:
            self.highscore = self.level
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
