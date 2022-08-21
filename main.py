from turtle import Screen
from player import Player
from car_creater import CarCreater
from scoreboard import  Scoreboard
import time
screen = Screen()
screen.setup(600,600)
screen.tracer(0)

player_1 = Player((-100,-280))
player_2 = Player((100,-280))
cars = CarCreater()
scoreboard = Scoreboard()



screen.listen()

screen.onkey(player_1.move_up , "w")
screen.onkey(player_2.move_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.create_cars()
    cars.move()
    screen.update()
    for car in cars.all_car:
        if player_1.distance(car)<20:
            player_1.restart()

        if player_2.distance(car)<20:
            player_2.restart()


    if player_1.ycor()> 230:
        scoreboard.increase_1()
        player_1.restart()

    if player_2.ycor()> 230:
        scoreboard.increase_2()
        player_2.restart()









screen.exitonclick()