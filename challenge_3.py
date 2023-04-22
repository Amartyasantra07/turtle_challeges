import random
import turtle as t
from turtle import Screen

cook = t.Turtle()

# geo_sides = 5
colour = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        cook.forward(100)
        cook.right(angle)


for shape_side_n in range(3, 11):
    cook.color(random.choice(colour))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
