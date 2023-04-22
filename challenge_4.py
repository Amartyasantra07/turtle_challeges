import random
import turtle as t

cook = t.Turtle()
t.colormode(255)


# colour=["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_tuple = (r, g, b)
    return random_color_tuple


directions = [0, 90, 180, 270]
cook.pensize(10)
cook.speed("fastest")

for _ in range(200):
    cook.color(random_color())
    cook.forward(30)
    cook.setheading(random.choice(directions))
