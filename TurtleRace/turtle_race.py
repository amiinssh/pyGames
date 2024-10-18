from turtle import Turtle, Screen
import random

is_race_on = False

tim = Turtle(shape="turtle")
tom = Turtle(shape="turtle")
bom = Turtle(shape="turtle")
num = Turtle(shape="turtle")
jum = Turtle(shape="turtle")
lum = Turtle(shape="turtle")

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Select a color:").strip().lower()

tim.color("green")
tim.penup()
tim.goto(x=-230, y=-100)

tom.color("blue")
tom.penup()
tom.goto(x=-230, y=-120)

bom.color("black")
bom.penup()
bom.goto(x=-230, y=-140)

num.color("orange")
num.penup()
num.goto(x=-230, y=-80)

jum.color("pink")
jum.penup()
jum.goto(x=-230, y=-60)

lum.color("yellow")
lum.penup()
lum.goto(x=-230, y=-40)

all_turtles = [tim, tom, bom, num, jum, lum]

if user_bet:
    is_race_on = True
else:
    print("You did not place a bet.")

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            print(f"The winning turtle color is: {winning_color}")

            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")
        
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
