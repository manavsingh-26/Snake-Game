import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen =  t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("light green")
screen.title("The Snake Game")
screen.tracer(0)
#screen.bgpic("unnamed.gif")

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()
        
    #Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.reset()
        snake.reset_snake()
        
    #Collision with Tail
    for seg in snake.segments[1:]:
        
        if snake.head.distance(seg) < 10:
            score.reset()
            snake.reset_snake()
            
            
    
    
     
screen.exitonclick()
t.done() 
