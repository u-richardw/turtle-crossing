import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
timmy = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True

screen.listen()
screen.onkey(timmy.move_up, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    #Detect collision
    for i in car_manager.cars:
        if i.distance(timmy) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect finish line
    if timmy.is_finish():
        timmy.go_start()
        car_manager.level()
        scoreboard.update()
        


screen.exitonclick()

