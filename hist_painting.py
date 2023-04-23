# import colorgram
# rgb = []
# color = colorgram.extract('image.jpg', 20)
# for colors in color:
#     r = colors.rgb.r
#     g = colors.rgb.g
#     b = colors.rgb.b
#     new_color=(r, g, b)
#     rgb.append(new_color)

import turtle as turtle_module
import random
from turtle import Screen
screen = Screen()


turtle_module.colormode(255)

cook = turtle_module.Turtle()
cook.speed("fastest")
cook.penup()
cook.hideturtle()
rgb_list = [(240, 245, 241), (202, 164, 109), (238, 240, 245), (150, 75, 49),
            (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71),
            (46, 122, 86),
            (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50)]

cook.setheading(225)
cook.forward(300)
cook.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    cook.dot(20, random.choice(rgb_list))
    cook.forward(50)
    if dot_count % 10 == 0:
        cook.setheading(90)
        cook.forward(50)
        cook.setheading(180)
        cook.forward(500)
        cook.setheading(0)


screen.exitonclick()