from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(-30,220)
        self.left_paddle_score = 0
        self.right_paddle_score = 0
        
    def score(self):
        self.write(f"{self.left_paddle_score} : {self.right_paddle_score}", align= "left", font= ("Arial", 50, "normal"))
        
    def updated_score(self):
        self.clear()
        self.score()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME-OVER", align= "center", font= ("Arial", 40, "normal"))
        
    