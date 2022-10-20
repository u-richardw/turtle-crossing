STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.go_start()
        self.left(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)
    def go_start(self):
        self.goto(STARTING_POSITION)
    def is_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False