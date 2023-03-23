from turtle import Turtle

class Ball(Turtle):
    def __init__(self, shape: str = "circle") -> None:
        super().__init__(shape)
        
        self.penup()
        self.color("white")
        
        self.x_pace = 10
        self.y_pace = 10
        
        
        
    def move(self):
        new_x = self.xcor() + self.x_pace
        new_y = self.ycor() + self.y_pace
        
        self.setpos(new_x, new_y)
        
        
    def near_wall(self) -> bool:
        ycor = self.ycor()
        
        if ycor >= 290 or ycor <= -290:
            return True
        
        
    def bounce(self, object: str):
        
        if object == "paddle":
            self.x_pace *= -1
        elif object == "wall":
            self.y_pace *= -1
            
            
    def out_of_bounds(self) -> bool:
        if self.xcor() >= 395 or self.xcor() <= -395:
            return True