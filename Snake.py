from turtle import Turtle

SEGMENTS_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self) :
        self.all_segments = []
        self.create_snakes()
        self.head = self.all_segments[0]

    def create_snakes(self):
        for position in SEGMENTS_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.all_segments.append(new_segment)


    def extend(self):
        self.add_segment(self.all_segments[-1].position())

    def move(self):
        for seg in range(len(self.all_segments) - 1, 0, -1):
            seg_x = self.all_segments[seg - 1].xcor()
            seg_y = self.all_segments[seg - 1].ycor()
            self.all_segments[seg].goto(seg_x, seg_y)
        self.head.forward(MOVING_SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

