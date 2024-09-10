from turtle import Turtle,Screen
import random
rgb_colors=["yellow", "gold", "orange", "red", "maroon", "violet",
            "magenta", "purple", "navy", "blue", "skyblue",
            "cyan", "turquoise","lightgreen",
            "green", "darkgreen", "chocolate", "brown", "black", "gray",
            ]

timmy=Turtle()
timmy.hideturtle()
timmy.penup()
timmy.speed(0)
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots=101
go=True
for _ in range(1,number_of_dots):
    timmy.dot(20, random.choice(rgb_colors))
    timmy.penup()
    timmy.forward(50)
    timmy.pendown()
    if  _% 10 ==0:
        timmy.penup()
        timmy.left(90)
        timmy.penup()
        timmy.forward(10)
        timmy.left(90)
        timmy.forward(500)
        timmy.right(90)
        timmy.forward(30)
        timmy.right(90)
















screen=Screen()
screen.exitonclick()
