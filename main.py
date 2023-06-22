from turtle import Screen
from snake import Snake
from food import Food
from scorecard import Scorecard
import time

screen = Screen()
screen.setup(500, 500)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake1 = Snake()
food1 = Food()
score1 = Scorecard()

screen.listen()
screen.onkey(snake1.up, "Up")
screen.onkey(snake1.down, "Down")
screen.onkey(snake1.left, "Left")
screen.onkey(snake1.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.15)

    snake1.move()

    #Collision with Food
    if snake1.head.distance(food1) < 18:
        food1.refresh()
        snake1.extend_snake()
        score1.count_score()

    #Detect Collision with wall
    if snake1.head.xcor() > 240 or snake1.head.xcor() < -240 or snake1.head.ycor() > 240 or snake1.head.ycor() < -240:
        #if abs(snake1.head.xcor())>240 or abs(snake1.head.ycor())>240:
        game_is_on = False
        score1.game_over()

    #Detect Collision with tail
    # for segment in snake1.snake_body:
    #     if snake1.head.distance(segment) < 10 and segment != snake1.head:
    #         game_is_on = False
    #         score1.game_over()

    for segment in snake1.snake_body[1:]:
        if snake1.head.distance(segment) < 10:
            game_is_on = False
            score1.game_over()

screen.exitonclick()