from turtle import Turtle
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_CONSTANT = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        # segment array keeps track of how many blocks we have in our snake, each block is an object "Snake"
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def move(self):
        # starting with len(self.segments) allows us to go in reverse order
        # start with the third block, move it to the coordinate of the second block, second block moves to
        # where the first block was at
        # -40,0 --> -20,0 --> 0,0
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # getting the x and y coordinate of the previous block
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # we care more about the head of the segment because if that change, the other block will follow
        self.head.forward(MOVE_CONSTANT)

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


    def add_segment(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]