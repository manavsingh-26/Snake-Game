import turtle as t

STARTING_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
   
    
    def __init__(self):
        self.segments =[]
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("dark green")
        self.head.shape("circle")
        self.head.shapesize(stretch_len=2)
        
    
    def create_snake(self):
        
        for pos in STARTING_POS:
            self.add_segment(pos)
    
   
    def move(self):
       
        for i in range(len(self.segments)-1,0,-1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y) 
  
        self.head.forward(MOVE_DISTANCE)
    
   
    def add_segment(self,pos):
        
        new_seg = t.Turtle("square")
        new_seg.color("green")
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)
        
    def reset_snake(self):
       
        for seg in self.segments:
            seg.hideturtle()
       
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("dark green")
        self.head.shape("circle")
        self.head.shapesize(stretch_len=2)
    
    def extend(self):
       
        self.add_segment(self.segments[-1].position())
        
    
    def up(self):
        
        if  self.head.heading()!= DOWN:
            self.head.setheading(UP)
    
    
    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)
    
    
    def left(self):
        
        if self.head.heading()!=RIGHT:        
            self.head.setheading(LEFT)
        
    
    def right(self):
        
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
                
        
        