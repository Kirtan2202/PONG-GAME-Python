from turtle import Turtle
MOVE = 20


class Paddle(Turtle):
    
    def __init__(self,position):
        super().__init__()
        self.position = position
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
        self.score = 0


    def move_up(self):
        new_y = self.ycor() + MOVE
        self.goto(self.xcor(),new_y)
    
    def move_down(self):
        new_y = self.ycor() - MOVE
        self.goto(self.xcor(),new_y)
        
    
        
        
        
        
    