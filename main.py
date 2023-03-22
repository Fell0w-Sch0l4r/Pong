from turtle import Screen, Turtle
from paddle import Paddle


screen = Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(width=800, height=600)
screen.tracer(0)


paddle = Paddle()
pc = Paddle(player="pc")



    


screen.listen()
screen.onkey(key="Up", fun=paddle.up)
screen.onkey(key="Down", fun=paddle.down)

while True:
    screen.update()



screen.exitonclick()