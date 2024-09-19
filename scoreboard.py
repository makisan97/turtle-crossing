from turtle import Turtle


FONT = ("Courier", 24, "normal")
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.hideturtle()
        self.goto(x=-220, y=250)
        self.score = 0
        self.write(f'Level: {self.score}', align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Level: {self.score}', align=ALIGNMENT, font=FONT)
        
    def game_over(self):
        self.goto(x=-50, y=0)
        self.clear()
        self.write(f'\tGAME OVER\n\tLevel: {self.score}', align=ALIGNMENT, font=FONT)