from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")

class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        
        self.color("white")
        self.hideturtle()
        self.penup()
        self.sety(200)
        
        self.r_score = 0
        self.l_score = 0
        
        self.update_score()
        
        
        
    def update_score(self):
        self.clear()
        
        self.text = f"{self.l_score}  |  {self.r_score}"
        self.write(arg=self.text, align=ALIGNMENT, font=FONT)
        
        
        
    def increase_score(self, paddle: str):
        if paddle == "rpaddle":
            self.r_score += 1
        elif paddle == "lpaddle":
            self.l_score += 1
            
        self.update_score()
        