import math
import random
import turtle

datafile="sample_data.txt"
viztitle="sample title"
WIDTH=800
HEIGHT=500


def count_observations(datafile):
    """This function takes as input the data file and returns as output the number of data observations in the file"""
#     linecount=0
#     #count the number of lines in the file using a loop
#     for linecount in open(f):
#         linecount+=1
#         print(linecount)
    with open(datafile) as sample:
        count = sum(1 for line in sample)
        print(int(count/3))
    #Divide the line count by 3 as each record takes 3 lines. Return the result
    return (int(count/3))
# count_observations()


def get_max_value(datafile,feature_no):
    """This function takes as input the data file and the feature to analyze and returns the maximum value of the given feature"""
      #declare a variable max to store the largest value of the feature. Initialize it to a very small number
    max=-99999
    with open(datafile) as datafile:
        for index,line in enumerate(datafile):
        
            if feature_no==1 and index%3==1:
            #If it is the first feature and we are at the line corresponding to the first feature
                if int(line)>max:
                #If the value of the data is greater than current max value, set max as current data value
                    max=int(line)
                   
            if feature_no==2 and index%3==2:
            #If it is the second feature and we are at the line corresponding to the second feature
                if int(line)>max:
                #If the value of the data is greater than current max value, set max as current data value
                    max=int(line)  
                   
    #Return the maximum value of given feature
        return max

get_max_value(datafile,1)

def draw_x_axis(pointer):
    """This function takes as input the turtle object and draws the x axis on screen. No return value."""
    #draw a horizontal line at bottom of screen which represents the x axis
    pointer.forward(WIDTH-50)

def draw_y_axis(pointer):
    """This function takes as input the turtle object and draws the y axis on screen. no return value."""
    pointer.home()
    #draw a vertical line at left of screen which represents the y axis
    pointer.left(90)
    pointer.forward(HEIGHT)

def draw_y_tickmark(pointer,datafile):
    """This function takes as input the turtle object and the datafile and draws the y axis ticks on screen. No return value."""
    pointer.home()
    pointer.left(90)
    #Get the maximum value of data corresponding to the feature to be plotted
    maxval=get_max_value(datafile,1)
    #Divide the maximum value obtained by the length of each y axis division (7) to obtain number of ticks
    yhighest=math.ceil(maxval/7)
    #Draw the ticks and the corresponding numbers using a loop
    for y in range(yhighest):
        pointer.forward(50)
        pointer.left(90)
        pointer.forward(5)
        pointer.penup()
        pointer.forward(40)
        pointer.pendown()
        pointer.write((y+1)*7, font=("Arial", 8, "normal"))
        pointer.penup()
        pointer.left(180)
        pointer.forward(40)
        pointer.pendown()
        pointer.forward(5)
        pointer.left(90)

def draw_x_labels(pointer,datafile):
    """This function takes as input the turtle object and the datafile and draws the x axis labels on screen. No return value."""
    pointer.home()
    #Count the number of observations in the data file
    data_count=count_observations(datafile)
    print("data count"+str(data_count))
    count = 0
    f = open(datafile)
    for line in f:
        if count%3==0:
            labelval=line.strip()
            pointer.forward(math.floor((WIDTH-100)/data_count))
            pointer.right(90)
            pointer.penup()
            pointer.forward(40)
            pointer.pendown()
            #print the label below the axis
            pointer.write(labelval, font=("Arial", 8, "normal"))
            pointer.penup()
            pointer.left(180)
            pointer.forward(40)
            pointer.right(90)
            pointer.pendown()
            
        count=count+1

def choose_color():
#     """This function when called returns a tuple of 3 values which are RGB values which can range from 0-255"""
#     #Using the randint function to generate a tuple of 3 random numbers between 0-255 which correspond to RGB color values for each bar in the chart.
#     return (random.randint(0,256),random.randint(0,256),random.randint(0,256))
#     #turtle.color("red", "green","blue")
    color = random.randint(1,6)
    if color == 1:
        #pointer.fillcolor("pink")
        return "Pink"
    elif color == 2:
        #pointer.fillcolor("lightblue")
        return "Blue"
    elif color == 3:
    #pointer.fillcolor("lightblue")
        return "Green"
    elif color == 4:
        #pointer.fillcolor("lightblue")
        return "Red"
    elif color == 5:
        #pointer.fillcolor("lightblue")
        return "Orange"
    else:
        #pointer.fillcolor("purple")
        return "Purple" 
                
def draw_bars(pointer,datafile):
    """This function takes as input the turtle object and the datafile and draws all the bars of the barchart on screen. No return value."""
    pointer.home()
    #Count the observations in the file
    obs=count_observations(datafile)
    t=1
    #loop over the data file to draw the bars on the chart corresponding to the values of the feature
    for i in range(obs):
        #Select random color for current bar to be drawn
        color=choose_color()
        #color=turtle.color("red", "green","blue")
        #color="red"
        #Draw rectangle at specified position on the chart, with height proportionate to data value of the current feature value
        #draw_rectangle(pointer,i*math.floor((WIDTH-100)/obs)+40,0,40,int(datafile[t]),color)
        #draw_rectangle(pointer,40,0,40,500,color)
        draw_rectangle(pointer,i*math.floor((WIDTH-100)/obs)+40,0,40,50,color)

        t=t+3
        
def draw_rectangle(pointer,px,py,width,height,pen_color):
    """This function takes as input the turtle object, the x and y coordinates of the rectangle position, the width and height of the rectangle, the rectangle color, and draws the rectangle on screen. No return value."""
    pointer.penup()
    pointer.home()
    #Set position of bar
    pointer.setpos(px,py)
    pointer.pendown()
    #set the color of the pen
    pointer.color(pen_color)
    #pointer.begin_fill()
    pointer.fillcolor("#DB148E")
    #draw a rectangle with the specified width and height
    for i in range(2):
        pointer.forward(width)
        pointer.left(90)
        pointer.forward(height*7)
        pointer.left(90)
    pointer.end_fill()
        
        
def turtleinit(datafile,viztitle):
    """This function takes as input the datafile and the bargraph title, initializes the turtle objects, creates the screen, and calls all the functions to create the bar graph. No return value."""
    #Initialize the screen
    wn=turtle.Screen()
    #Set the title of the bar graph
    wn.title(viztitle)
    #Set the width and height of window
    turtle.setup(width=WIDTH,height=HEIGHT,startx=0,starty=0)
    #Set the default position of the turtle pointer to be the bottom left and not centre
    turtle.setworldcoordinates(-100,-100,WIDTH,HEIGHT)
    #Set the color modes and speed of the turtle pointer
    turtle.colormode(255)
    turtle.speed(0)
    #Initialize a Turtle object to draw with
    pointer=turtle.Turtle()
    #Call the individual functions to plot the bar graph
    draw_x_axis(pointer)
    draw_y_axis(pointer)
    draw_y_tickmark(pointer,datafile)
    draw_x_labels(pointer,datafile)
    draw_bars(pointer,datafile)

    wn.mainloop()
    
turtleinit(datafile,viztitle)