from turtle import Turtle, Screen
import prettytable
timmy = Turtle()
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
timmy.shape("turtle")
timmy.color('DarkSeaGreen')
# timmy.penup()
for i in range(3):
    timmy.forward(100)
    timmy.left(120)
    timmy.forward(100)


my_screen.exitonclick()