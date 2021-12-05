# Bouncing Balls Simulation Program

import turtle
from turtle import Turtle, Screen
import random
from createDrunks import createDrunks
import math

# Drunkard class

class drunkard(Turtle):
    def __init__(self, color, speed, xpos, ypos):
        self.turtle = turtle.Turtle()
        self.turtle.shape('circle')
        self.turtle.fillcolor(color)
        self.turtle.speed(speed)
        self.turtle.setx(xpos)
        self.startxcor = xpos
        self.turtle.sety(ypos)
        self.startycor = ypos
        self.dist = 0
    


    

# change edges to remove unavailable directions

def atLeftEdge(ball, screen_width):
    if ball.xcor() < -screen_width / 2:
        return True
    else:
        return False

def atRightEdge(ball, screen_width):
    if ball.xcor() > screen_width / 2:
        return True
    else:
        return False

def atTopEdge(ball, screen_height):
    if ball.ycor() > screen_height / 2:
        return True
    else:
        return False

def atBottomEdge(ball, screen_height):
    if ball.ycor() < -screen_height / 2:
        return True
    else:
        return False

# Randomize directions
# change to change direction, update with random direction based on instructions

def change_position(drunk, dir, stepSize):
    DIRECTIONS = (NORTH,NORTHEAST,EAST,SOUTHEAST,SOUTH,SOUTHWEST,WEST,NORTHWEST) = (0,45, 90,135, 180, 225, 270, 315)
    drunk.turtle.setheading(random.choice(DIRECTIONS))
    drunk.turtle.forward(stepSize)

# Calculate Distance

def distance(drunk):
    x = drunk.startxcor - drunk.turtle.xcor
    y = drunk.startycor - drunk.turtle.ycor
    dist = math.sqrt(x**2 + y**2)    
    return dist
    
    
    
#Create Drunkards
#change
# ---- main
# program greeting
print('This program simulates drunkards walk in a turtle screen')
print('for a specified number of steps.')

# init screen size
screen_width = 800
screen_height = 600
turtle.setup(screen_width,screen_height)

# create turtle window
window = turtle.Screen()
window.title('Drunkards Walk')

# prompt user for number of balls and steps
#change to number of moves
num_steps = int(input('Enter number of steps to run: '))
num_drunks = 3

# create balls
create = []
create = createDrunks()
drunk1 = drunkard(create[0], create[1], create[2], create[3])
create = createDrunks()
drunk2 = drunkard(create[0], create[1], create[2], create[3])
create = createDrunks()
drunk3 = drunkard(create[0], create[1], create[2], create[3])

# set start time
#start_time = time.time()

# begin simulation
terminate = False

#update with number of moves
print(num_steps)
#Needs to be setting the direction 


def drunkards_walk(step_size, steps):
    # Assumes turtle.mode('standard')
    DIRECTIONS = (NORTH,NORTHEAST,EAST,SOUTHEAST,SOUTH,SOUTHWEST,WEST,NORTHWEST) = (0,45, 90,135, 180, 225, 270, 315)
    turtle.setheading(random.choice(DIRECTIONS))
    turtle.forward(step_size)


#def make_drunkard_walk(step_size,step_number):
#    for i in range(step_size,step_number):
#        turtle.setheading(90*random.randint(0,3))
#        turtle.forward(step_size)

# add equation for distance from start point
#Math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

print("In", num_steps, "steps Drunk 1 moves", drunk1.dist)
print("In", num_steps, "steps Drunk 2 moves", drunk2.dist)
print("In", num_steps, "steps Drunk 3 moves", drunk3.dist)

# exit on close window
turtle.exitonclick()
