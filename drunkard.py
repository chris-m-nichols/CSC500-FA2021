# Bouncing Balls Simulation Program

import turtle
from turtle import Turtle, Screen
import random


# Drunkard class

class drunkard(Turtle):
    def __init__(self, color, speed, xpos, ypos):
        turtle.shape('circle')
        turtle.fillcolor(color)
        turtle.speed(speed)
        turtle.setx(xpos)
        startxcor = xpos
        turtle.sety(ypos)
        startycor = ypos
    
    def change_position(dir, stepSize):
        turtle.setheading(dir)
        turtle.forward(stepSize)
    
# Create drunkards

def createDrunks(num_drunks):
    colorList = ['red', 'green', 'blue', 'black', 'purple', 'teal', 'yellow']
    xcords = [-40, 0, 40]
    ycords = [-40, 0, 40]
    dict_ = {}
    for k in range(0, num_drunks):
        ballColor = random.choice(colorList)
        speed = 1
        xcord = random.choice(xcords)
        ycord = random.choice(ycords)
        dict_['string%s' % k] = drunkard(ballColor, speed, xcord, ycord)

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

#change to change direction, update with random direction based on instructions

    
    
    
    
#Create Drunkard

def createBalls(num_balls):
    balls = []
    colorList = ['red', 'green', 'blue', 'black', 'purple', 'teal', 'yellow']
    xcords = [-40, 0, 40]
    ycords = [-40, 0, 40]
    
    #locations = [(40,40), (40,0), (40,-40), (0,40), (0,0), (0, -40), (-40,40), (-40,0), (-40,-40)]
    for k in range(0, num_balls):
        shape = 'circle'
        ballColor = random.choice(colorList)
        speed = 0
        xcord = random.choice(xcords)
        ycord = random.choice(ycords)

        #new_ball.setheading(random.randint(1,359))
    #    new_ball.pos(random.choice(locations))
        

    return balls
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
createDrunks(num_drunks)

# set start time
#start_time = time.time()

# begin simulation
terminate = False

#update with number of moves

#Needs to be setting the direction 


def drunkards_walk(step_size, steps):
    # Assumes turtle.mode('standard')
    DIRECTIONS = (EAST, NORTH, WEST, SOUTH) = (0, 90, 180, 270)
    for _ in range(steps):
        #go(random.choice(DIRECTIONS), step_size)
        turtle.setheading(DIRECTIONS)
        turtle.forward(step_size)

#def make_drunkard_walk(step_size,step_number):
#    for i in range(step_size,step_number):
#        turtle.setheading(90*random.randint(0,3))
#        turtle.forward(step_size)

# add equation for distance from start point


# exit on close window
turtle.exitonclick()
