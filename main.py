from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)    #setting up the width and height of the screen
user_bet = screen.textinput(
    title="Make your bet",
    prompt="Which turtle will win the race? Choose from: red, orange, yellow, green, blue, purple"
)

if user_bet:
    user_bet = user_bet.strip().lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet and user_bet in colors:                #using the is_race_on before the while loop and declaring it true outside the while loop, we prevent our while loop from starting up while the user is still deciding on which turtle they're going to bet on, so it dosen't start prematurely
    is_race_on = True
else:
    print("Please enter a valid turtle color.")   
    screen.bye()

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            result_turtle = Turtle()
            result_turtle.hideturtle()
            result_turtle.penup()
            result_turtle.goto(0, 140)
            
            result_turtle.write(
                f"{winning_color.title()} Turtle Wins!",
                align="center",
                font=("Arial", 16, "bold")
            )

            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner !")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner !")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

