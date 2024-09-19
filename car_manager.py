from turtle import Turtle
import random


COLORS = ["red", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, level):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.goto(x=280, y=random.randint(-250, 250))
        #self.speed = self.get_speed()
        self.speed = STARTING_MOVE_DISTANCE + level * MOVE_INCREMENT

    def move(self):
        next_x = self.xcor() - self.speed
        self.goto(x=next_x, y=self.ycor())
        
        
        
    # def increase_speed(self):
    #     return (self.speed + MOVE_INCREMENT)
    
    # def get_speed(self):
    #     return (STARTING_MOVE_DISTANCE + scoreboard.sccore * MOVE_INCREMENT)
        
    

        


        
            
