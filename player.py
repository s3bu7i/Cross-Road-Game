from turtle import Turtle

class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.player_position = position
        self.goto(self.player_position)
        self.color("blue")

    def move_up(self):
        self.forward(10)

    def restart(self):
        self.goto(self.player_position )

