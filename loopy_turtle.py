## Turtle setup
import turtle

window = turtle.Screen()
window.title("Loopy Turtle")
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
window.setworldcoordinates(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

## Create the turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.pensize(2)
my_turtle.speed("normal")

## Drawing
my_turtle.penup()
my_turtle.goto(100,20)
my_turtle.pendown()

num_side=8
for side_num in range(num_side):
    my_turtle.forward(50)
    my_turtle.left(360/num_side)

## Run the window
window.mainloop()