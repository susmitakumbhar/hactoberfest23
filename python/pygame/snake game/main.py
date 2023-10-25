from food import Food
from score import Score
from snake import Snake as s
import turtle as t
import time
scr = t.Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)
snake = s()
food = Food()
score = Score()

scr.listen()
t.onkey(snake.up, "Up")
t.onkey(snake.down, "Down")
t.onkey(snake.right, "Right")
t.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    scr.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 10:
        food.refresh()
        score.update()
        score.printScore()
        snake.extend()
    if snake.head.xcor() > 300 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300:
        score.gameOver()
        is_game_on = False
    for i in range(1,len(snake.box[1:])):
        if snake.head.distance(snake.box[i].position()) < 5:
            is_game_on = False
scr.exitonclick()