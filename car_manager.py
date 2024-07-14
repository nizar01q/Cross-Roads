from turtle import Turtle
import random
import time

COLORS = ["whitesmoke", "navy", "deep pink", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 6
MOVE_INCREMENT = 3


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.starting_move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.goto(320, random.randint(-248, 248))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_cars(self):
        for i in range(len(self.all_cars)):
            self.all_cars[i].forward(self.starting_move_distance)

    def increase_speed(self):
        self.starting_move_distance += MOVE_INCREMENT








