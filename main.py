import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.title('Turtle Crossing')
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, 'Up')
screen.onkeypress(player.move_down, 'Down')


cars = []
loop = 0
level = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    # Randomly create new car

    chance_to_create_car = random.randint(1, 5)
    if chance_to_create_car == 5:
        car = CarManager(level)
        cars.append(car)
    
    for car in cars:
        car.move()
    
    if player.ycor() == 280:
        player.reach_finish()
        scoreboard.increase_score()
        level += 1
        
    # Detect collision with car
    for car in cars:
        if player.distance(car) < 20:
            game_is_on = False
            player.collision()
            scoreboard.game_over()

            
            
            
            
            
            
screen.exitonclick()
    