from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier",25,"normal")

class Score(Turtle):
    
    def __init__(self):
       
        super().__init__()
        self.hideturtle()
        self.penup()
        self.points =0
        self.high_score = 0
        self.color("black")
        self.goto(-20,260)
        self.write(f"Score:{self.points}||High Score:{self.high_score}",align=ALIGNMENT,font=FONT)         
        
        
    def update(self):
     
        
        self.clear()
        self.goto(-20,260)
        self.write(f"Score:{self.points}||High Score:{self.high_score}",align=ALIGNMENT,font=FONT)
   
    
    def reset(self):
        
        if self.points > self.high_score:
            self.high_score = self.points
        self.points = 0
        self.update()
        
    
    def increase_score(self):
        self.points+=1
        self.update()
    
#  
#        
        
        
        
        
        
        