from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep


screen = Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(width=800, height=600)
screen.tracer(0)


r_paddle = Paddle()
l_paddle = Paddle(side="left")

ball = Ball()



    


screen.listen()
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s ", fun=l_paddle.down)

while True:
    sleep(0.05)
    screen.update()
    ball.move()
    
    if ball.near_wall():
        ball.bounce("wall")
        
    if ball.distance(r_paddle) <= 25 or ball.distance(l_paddle) <= 25:
        ball.bounce("paddle")



screen.exitonclick()