from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.allcars = []
        self.carspeed = 5

    def spawn(self):
        newcar = Turtle("square")
        newcar.penup()
        newcar.speed("fastest")
        newcar.shapesize(1, 2)
        newcar.color(random.choice(COLORS))
        newcar.goto(280, random.randint(-250, 250))
        self.allcars.append(newcar)

    def move(self):
        for car in self.allcars:
            car.backward(self.carspeed)

    def newlvl(self):
        self.carspeed += 10
