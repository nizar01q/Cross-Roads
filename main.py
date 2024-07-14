import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import pygame
pygame.init()
sound1 = pygame.mixer.Sound("gameover.wav")
sound2 = pygame.mixer.Sound("levelup.wav")

screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("roads.png")
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    if player.ycor() > 290:
        player.level_up()
        cars.increase_speed()
        scoreboard.increase_score()
        sound2.play()

    for car in cars.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            sound1.play()


screen.exitonclick()