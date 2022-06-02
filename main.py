from turtle import Turtle, Screen
import random

screen = Screen()
choice = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "yellow", "purple", "orange", "green"]
your_position = [-70, -40, -10, 20, 50, 80]
list_race = []

for i in range(6):
    name_turtle = Turtle(shape="turtle")
    name_turtle.color(colors[i])
    name_turtle.penup()
    name_turtle.goto(x=-250, y=your_position[i])
    list_race.append(name_turtle)


if choice:
    is_on = True

while is_on:

    for j in list_race:
        if j.xcor() > 310:
            is_on = False
            winning = j.pencolor()
            if winning == choice:
                print(f"You've won! The {winning} turtle is the winner!")
            else:
                print(f"You've lost! The {winning} turtle is the winner!")
        rand_distancion = random.randint(0, 10)
        j.forward(rand_distancion)




screen.exitonclick()
