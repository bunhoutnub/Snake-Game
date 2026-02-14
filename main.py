# use import turtle so that I can create pictures
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#setting up the screen
screen = Screen()
screen.setup(width=600, height=600) #screen size
screen.bgcolor("#16213e") #ocean dark blue background to match web version
screen.title("Snake Game") #game title
screen.tracer(0)#set tracer to 0 to turn pen off

snake = Snake() #call the Snake class from snake.py file
food = Food() #call the Food class from food.py file
scoreboard = Scoreboard() #call the Scoreboard class from scoreboard.py file

screen.listen() #make the game listening for keystrokes
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

#get the snake to automatically move
game_is_on = True
while game_is_on:
    screen.update() # update the screen once all the segments have moved forward
    time.sleep(0.08) # faster delay for smoother movement
    snake.move()
  
    #detect collision with food     
    if snake.head.distance(food) < 20:
        food.refresh() 
        scoreboard.increase_score()
        snake.extend()
        
    #detect collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #detect collision with the tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
    #if head collides with any segments in the tail:
        # GAME OVER!
        
        
        
screen.exitonclick()