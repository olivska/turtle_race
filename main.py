from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? enter the color: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "violet"]

y_position = [150, 100, 50, 0, -50, -100, -150]
all_turtles = []

for turtle_index in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You lost. The {winning_turtle} turtle is the winner.")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
