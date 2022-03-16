import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
player = Player()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(player.player_movement, "Up")

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.movement()
    car.create_car()
    for cars in car.all_cars:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > 280:
        car.update_speed()
        player.restart()
        car.update_speed()
        scoreboard.reach_end()
screen.exitonclick()












