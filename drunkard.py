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
        self.startxcor = 0
        self.startycor = 0
    
    def set_startxcor(self, xcor):
        self.startxcor = xcor

    def set_startycor(self, ycor):
        self.startycor = ycor

    def get_startxcor(self):
        return self.startxcor
    
    def get_startycor(self):
        return self.startycor

    

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

def change_position(drunk, stepSize):
    DIRECTIONS = (NORTH,NORTHEAST,EAST,SOUTHEAST,SOUTH,SOUTHWEST,WEST,NORTHWEST) = (0,45, 90,135, 180, 225, 270, 315)
    drunk.turtle.setheading(random.choice(DIRECTIONS))
    drunk.turtle.forward(stepSize)

# Calculate Distance

def distance(drunk):
    dist = drunk.turtle.distance(drunk.get_startxcor(),drunk.get_startycor())
    #x1 = drunk.get_startxcor
    #x2 = drunk.turtle.xcor
    #print(drunk.turtle.position)
    #print(drunk.turtle.xcor)
    #x = int(x1) - int(x2)
    #y1 = drunk.get_startycor
    #y2 = drunk.turtle.ycor
    #y = int(y1) - int(y2)
    #dist = math.sqrt(x**2 + y**2)    
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
stepSize = 40

# create balls
create = []
create = createDrunks()
drunk1 = drunkard(create[0], create[1], create[2], create[3])
drunk1.turtle.shape('circle')
drunk1.turtle.fillcolor(create[0])
drunk1.turtle.speed(create[1])
drunk1.turtle.setx(create[2])
drunk1.set_startxcor(create[2])
drunk1.turtle.sety(create[3])
drunk1.set_startycor(create[3])

create = createDrunks()
drunk2 = drunkard(create[0], create[1], create[2], create[3])
drunk2.turtle.shape('circle')
drunk2.turtle.fillcolor(create[0])
drunk2.turtle.speed(create[1])
drunk2.turtle.setx(create[2])
drunk2.set_startxcor(create[2])
drunk2.turtle.sety(create[3])
drunk2.set_startycor(create[3])

create = createDrunks()
drunk3 = drunkard(create[0], create[1], create[2], create[3])
drunk3.turtle.shape('circle')
drunk3.turtle.fillcolor(create[0])
drunk3.turtle.speed(create[1])
drunk3.turtle.setx(create[2])
drunk3.set_startxcor(create[2])
drunk3.turtle.sety(create[3])
drunk3.set_startycor(create[3])

# set start time
#start_time = time.time()

# begin simulation
terminate = False

#update with number of moves
print(num_steps)
for k in range(num_steps):
    change_position(drunk1, stepSize)
for k in range(num_steps):
    change_position(drunk2, stepSize)
for k in range(num_steps):
    change_position(drunk3, stepSize)


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

print("In", num_steps, "steps Drunk 1 moves", distance(drunk1))
print("In", num_steps, "steps Drunk 2 moves", distance(drunk2))
print("In", num_steps, "steps Drunk 3 moves", distance(drunk3))

# exit on close window
turtle.exitonclick()
