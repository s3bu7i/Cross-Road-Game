from turtle import Turtle, colormode
import random

colormode(255)

class CarCreater:
    def __init__(self):
        self.all_car=[]


    def create_cars(self):
        random_number = random.randint(1,5)
        if random_number == 1:
            new_car  = Turtle()
            new_car.shape("square")
            new_car.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
            new_car.penup()
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.goto(300 ,random.randint(-200,200))
            self.all_car.append(new_car)

    def move(self):
        for car in self.all_car:
            car.backward(10)
