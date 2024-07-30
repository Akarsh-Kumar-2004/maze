import turtle
from ball import Ball



screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width = 800,height = 600)
screen.title("ESCAPE THE MAZE")
# screen.tracer(0)
#ball = Ball()

ring = turtle.Turtle()
ring.color("white")
ring.pensize(4)
clr = ["red","green","blue","yellow","pink","pink"]
ring.speed(0)
for i in range(1):
    ring.circle(30*i)
    ring.up()
    ring.color(clr[i])
    ring.goto(0,-30*i)
    ring.down()
    
    
    
screen.exitonclick()
