import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
score = Scoreboard()

screen.onkey(fun=player.move, key="w")

count =0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    count+=1
    if count%3 == 0:
        car.spawn()
    car.move()

    # player reaches the end
    if player.ycor() > 270:
        player.new_level()
        car.newlvl()
        score.update_score()

    # collision with car
    for cars in car.allcars:
        if cars.distance(player) < 20:
            score.gameover()
            game_is_on = False

screen.exitonclick()
