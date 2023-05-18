from turtle import Turtle,Screen
import time
from snake import Snake

my_screen =Screen()
my_screen.setup(600*600)
my_screen.bgcolor("black")
my_screen.title("SNAKE")
my_screen.tracer(0)

snake=Snake() 

my_screen.listen()
my_screen.onkey(snake.up,"Up")
my_screen.onkey(snake.down,"Down")
my_screen.onkey(snake.left,"Left")
my_screen.onkey(snake.right,"Right")

game_on = True

while game_on:
    my_screen.update()
    time.sleep(0.1)
    
    snake.move()

        
        
    

my_screen.exitonclick()