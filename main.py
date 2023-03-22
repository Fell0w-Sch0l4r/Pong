from turtle import Screen
from paddle import Paddle


screen = Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(width=800, height=600)
screen.tracer(0)


r_paddle = Paddle()
l_paddle = Paddle(side="left")



    


screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s ", fun=l_paddle.down)

while True:
    screen.update()



screen.exitonclick()