
from turtle import Turtle, Screen

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__ (self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POS:
        # for num in range(3):
            self.add_segment(position)

    def add_segment(self, position): #def add_seg(self, num)
        new_snake = Turtle("square")
        new_snake.speed("fastest")
        new_snake.color("white")
        new_snake.penup()
        # new_snake.backward(20 * num)
        # new_snake.goto(-MOVE_DISTANCE * num, 0)
        new_snake.goto(position) # if list of tuple nad for position is used
        self.snake_body.append(new_snake)

    def extend_snake(self):
        self.add_segment(self.snake_body[-1].position())



    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):   # 2, 0, -1
            # new_x = snake_body[seg_num - 1].xcor()
            # new_y = snake_body[seg_num - 1].ycor()
            snake_position = self.snake_body[seg_num - 1].position()
            self.snake_body[seg_num].goto(snake_position)

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