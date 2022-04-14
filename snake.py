from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        # setting head must happen after create_snake
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            # new_segment = Turtle(shape="square")
            # new_segment.color("white")
            # new_segment.penup()
            # new_segment.goto(position)
            new_segment = self.create_segment()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        # the last element of the snake to take the "state" of the element just before
        # only the first element gets a new state
        # we need to loop over each segment, starting from the last one, up to the first one
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # get coordinates of previous segment
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # move last segment to new coordinates and repeat for each segment
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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

    def create_segment(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        return new_segment

    def add_segment(self):
        new_segment = self.create_segment()
        last_seg_x = self.segments[-1].xcor()
        last_seg_y = self.segments[-1].ycor()
        new_segment.goto(last_seg_x, last_seg_y)
        self.segments.append(new_segment)

    def reset(self):
        # doesn't remove the snake from the screen just yet
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
