from turtle import Turtle, Screen

cook = Turtle()
screen = Screen()


def move_forward():
    cook.forward(10)


def move_backward():
    cook.backward(10)


def turn_left():
    new_heading = cook.heading() + 10
    cook.setheading(new_heading)


def turn_right():
    new_heading = cook.heading() - 10
    cook.setheading(new_heading)


def clear():
    cook.clear()
    cook.penup()
    cook.home()
    cook.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
