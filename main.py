from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
POSITION = [(350,0), (-350,0)]


screen = Screen()
screen.bgcolor("black")
screen.title("PONG GAME")
screen.setup(width=800, height=600)
screen.tracer(0)


right_paddle = Paddle(POSITION[0])
left_paddle = Paddle(POSITION[1])


ball = Ball()
scoreboard = Scoreboard()
game_over = Scoreboard()
game_over.color("Blue")


screen.listen()
screen.onkey(right_paddle.move_up,"Up")
screen.onkey(right_paddle.move_down,"Down")
screen.onkey(left_paddle.move_up,"w")
screen.onkey(left_paddle.move_down,"s")    
  
game_is_on = True

while game_is_on:    #if we end the animation with tracer 0, then we need to manually update screen every time(while loop)
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()
        
    #detect collision with paddle 
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
        
    #detect collision with wall and reset the ball in opposite direction
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_paddle_score += 1
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_paddle_score += 1
        
    if scoreboard.left_paddle_score > 4 or scoreboard.right_paddle_score > 4:
        game_over.game_over()
        game_is_on = False
        
    scoreboard.updated_score()
        
        
        

screen.exitonclick()