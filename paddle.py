from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, shape: str = "square", side: str = "right") -> None:
        super().__init__(shape)
        
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        
        if side == "right":
            self.setx(x=350)
        elif side == "left":
            self.setx(x=-350)
        
        
        
        
    def up(self):
        if self.ycor() < 240:
            self.sety(self.ycor() + 20)
            
    def down(self):
        if self.ycor() > -240:
            self.sety(self.ycor() - 20)
        