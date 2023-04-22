import random
import turtle as t

cook = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_tuple = (r, g, b)
    return random_color_tuple


cook.speed("fastest")


def draw_spiral(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        cook.color(random_color())
        cook.circle(100)
        cook.setheading(cook.heading() + size_of_gap)


draw_spiral(5)
screen = t.Screen()
screen.exitonclick()
