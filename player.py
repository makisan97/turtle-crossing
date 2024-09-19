from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()
        self.setheading(90)
        self.goto(x=0, y=-280)

    def move_up(self):
        next_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=self.xcor(), y=next_y)
        
    def move_down(self):
        next_y = self.ycor() - MOVE_DISTANCE
        self.goto(x=self.xcor(), y=next_y)
        
    def reach_finish(self):
        print('reach finish')
        self.goto(x=0, y=-280)
        
    def collision(self):
        self.goto(x=0, y=-280)