from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, shape: str = "square", player: str = "user") -> None:
        super().__init__(shape)
        
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        
        if player == "user":
            self.setx(x=350)
        else:
            self.setx(x=-350)
        
        
        
        
    def up(self):
        if self.ycor() < 240:
            self.sety(self.ycor() + 20)
            
    def down(self):
        if self.ycor() > -240:
            self.sety(self.ycor() - 20)
        