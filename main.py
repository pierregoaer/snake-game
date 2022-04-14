from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    snake.move()
    screen.update()
    time.sleep(.1)

    # detect collisions with food using turtle.distance
    if snake.head.distance(food) < 15:
        snake.add_segment()
        food.new_location()
        score.increase_score()

    # detect collisions with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # detect collisions with tail
    for segment in snake.segments[1:]:
        # slicing bc would trigger everytime because snake.segments[0] == snake.head
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()
