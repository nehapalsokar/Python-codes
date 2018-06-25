# A module for drawing a chart with the turtle
import turtle  # import module

# Define window size as constants
window = turtle.Screen()  # create a window for the turtle to draw on
window.title("Turtle Demo")  # the title to show at the top of the window
WINDOW_WIDTH = 400  # size constants for easy changing
WINDOW_HEIGHT = 300
window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)  # set window size (width, height)
window.setworldcoordinates(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)  # coord system

# # Create the turtle
my_turtle = turtle.Turtle()
my_turtle.speed("fast")  # how fast the turtle should move

my_turtle.penup()
my_turtle.goto(100, 100)
my_turtle.pendown()     # start drawing again
my_turtle.forward(100)


# # Move the turtle to draw
my_turtle.left(60)      # turn left
my_turtle.forward(120)  # move forward
my_turtle.right(120)    # turn left
my_turtle.forward(120)  # move forward

# Make turtle graphics appear and run; wait for the user to close the screen
# This MUST be the last statement executed in the script
window.mainloop()