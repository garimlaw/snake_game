from turtle import Turtle

START_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_INSTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for pos in START_POSITION:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(pos)
            self.segments.append(segment)
    
    def move(self):
        for seg_num in range(len(self.segments) - 1,0,-1): #move snake
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_INSTANCE)
