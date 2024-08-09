from turtle import Turtle, Screen
import prettytable
timmy = Turtle()
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
timmy.shape("turtle")
timmy.color('CornflowerBlue')
timmy.penup()
timmy.forward(120)

my_screen.exitonclick()