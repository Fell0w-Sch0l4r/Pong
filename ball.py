from turtle import Turtle

class Ball(Turtle):
    def __init__(self, shape: str = "circle") -> None:
        super().__init__(shape)
        
        self.penup()
        self.color("white")
        
        
        
    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        
        self.setpos(new_x, new_y)