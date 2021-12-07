# Bouncing Balls Simulation Program

import turtle
import random
from createDrunks import createDrunks
import math

# Drunkard class

class drunkard(turtle.Turtle):
    def __init__(self, color, speed, xpos, ypos):
        self.createTurtle()
        self.startxcor = 0
        self.startycor = 0

    def createTurtle(self):
        self.turtle = turtle.Turtle()

    def get_xCor(self):
        return self.turtle.xcor()

    def get_yCor(self):
        return self.turtle.ycor()
    
    def set_startxcor(self, xcor):
        self.startxcor = xcor

    def set_startycor(self, ycor):
        self.startycor = ycor

    def get_startxcor(self):
        return self.startxcor
    
    def get_startycor(self):
        return self.startycor

    

# change edges to remove unavailable directions

def atLeftEdge(drunk, screen_width):
    if drunk == 1:
        xcor = drunk1.get_xCor() - stepSize
    elif drunk == 2:
        xcor = drunk2.get_xCor() - stepSize
    elif drunk == 3:
        xcor = drunk3.get_xCor() - stepSize
    if xcor < -(screen_width / 2):
        return True
    else:
        return False

def atRightEdge(drunk, screen_width):
    if drunk == 1:
        xcor = drunk1.get_xCor() + stepSize
    elif drunk == 2:
        xcor = drunk2.get_xCor() + stepSize
    elif drunk == 3:
        xcor = drunk3.get_xCor() + stepSize
    if xcor > (screen_width / 2):
        return True
    else:
        return False

def atTopEdge(drunk, screen_height):
    if drunk == 1:
        ycor = drunk1.get_yCor() + stepSize
    elif drunk == 2:
        ycor = drunk2.get_yCor() + stepSize
    elif drunk == 3:
        ycor = drunk3.get_yCor() + stepSize
    if ycor > (screen_height / 2):
        return True
    else:
        return False

def atBottomEdge(drunk, screen_height):
    if drunk == 1:
        ycor = drunk1.get_yCor() - stepSize
    elif drunk == 2:
        ycor = drunk2.get_yCor() - stepSize
    elif drunk == 3:
        ycor = drunk3.get_yCor() - stepSize
    if ycor < -(screen_height / 2):
        return True
    else:
        return False

# Randomize directions
# change to change direction, update with random direction based on instructions

def change_position(drunk, stepSize ,width,height):
    DIRECTIONS = [0,45, 90, 135, 180, 225, 270, 315]
    if atLeftEdge(drunk,width):
            DIRECTIONS.remove(225) 
            DIRECTIONS.remove(270)
            DIRECTIONS.remove(315)     
    if atRightEdge(drunk,width): 
            DIRECTIONS.remove(45)
            DIRECTIONS.remove(90)
            DIRECTIONS.remove(135)
    if atBottomEdge(drunk,height): 
        try:
            DIRECTIONS.remove(135)
        except:
            pass
        DIRECTIONS.remove(180)
        try:
            DIRECTIONS.remove(225)
        except:
            pass
    if atTopEdge(drunk,height):
        try:
            DIRECTIONS.remove(0)
        except:
            pass
        try:
            DIRECTIONS.remove(45)
        except:
            pass
        try:
            DIRECTIONS.remove(315)
        except:
            pass
    if drunk == 1:
        drunk1.turtle.setheading(random.choice(DIRECTIONS))
        drunk1.turtle.forward(stepSize)
    elif drunk == 2:
        drunk2.turtle.setheading(random.choice(DIRECTIONS))
        drunk2.turtle.forward(stepSize)
    elif drunk == 3:
        drunk3.turtle.setheading(random.choice(DIRECTIONS))
        drunk3.turtle.forward(stepSize)


        

# Calculate Distance

def distance(drunk):
    if drunk == 1:
        dist = math.sqrt((drunk1.get_startxcor() - drunk1.turtle.xcor()) ** 2 + (drunk1.get_startycor() - drunk1.turtle.ycor()) ** 2)   
    elif drunk == 2:
        dist = math.sqrt((drunk2.get_startxcor() - drunk2.turtle.xcor()) ** 2 + (drunk2.get_startycor() - drunk2.turtle.ycor()) ** 2)
    elif drunk == 3:
        dist = math.sqrt((drunk3.get_startxcor() - drunk3.turtle.xcor()) ** 2 + (drunk3.get_startycor() - drunk3.turtle.ycor()) ** 2)
    return dist
    
    
    
#Create Drunkards
#change
# ---- main
# program greeting
print('This program simulates drunkards walk in a turtle screen')
print('for a specified number of steps.')

# init screen size
screen_width = 600
screen_height = 400
turtle.setup(screen_width,screen_height)

# Set angle orientation
turtle.mode("logo")

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
create = createDrunks(screen_width, screen_height)
drunk1 = drunkard(create[0], create[1], create[2], create[3])
drunk1.turtle.shape('circle')
drunk1.turtle.fillcolor(create[0])
drunk1.turtle.speed(create[1])
turtle.penup()
drunk1.turtle.setx(create[2])
drunk1.set_startxcor(create[2])
drunk1.turtle.sety(create[3])
drunk1.set_startycor(create[3])
turtle.pendown()

create = createDrunks(screen_width, screen_height)
drunk2 = drunkard(create[0], create[1], create[2], create[3])
drunk2.turtle.shape('circle')
drunk2.turtle.fillcolor(create[0])
drunk2.turtle.speed(create[1])
turtle.penup()
drunk2.turtle.setx(create[2])
drunk2.set_startxcor(create[2])
drunk2.turtle.sety(create[3])
drunk2.set_startycor(create[3])
turtle.pendown()

create = createDrunks(screen_width, screen_height)
drunk3 = drunkard(create[0], create[1], create[2], create[3])
drunk3.turtle.shape('circle')
drunk3.turtle.fillcolor(create[0])
drunk3.turtle.speed(create[1])
turtle.penup
drunk3.turtle.setx(create[2])
drunk3.set_startxcor(create[2])
drunk3.turtle.sety(create[3])
drunk3.set_startycor(create[3])
turtle.pendown

# begin simulation
terminate = False

#update with number of moves
print(num_steps)
for k in range(num_steps):
    drunk = 1
    change_position(drunk, stepSize,screen_width,screen_height)
    drunk = 2
    change_position(drunk, stepSize,screen_width,screen_height)
    drunk = 3
    change_position(drunk, stepSize,screen_width,screen_height)

# add equation for distance from start point
#Math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

drunk = 1
print("In", num_steps, "steps Drunk 1 moves", distance(drunk), "pixels.")
drunk = 2
print("In", num_steps, "steps Drunk 2 moves", distance(drunk), "pixels.")
drunk = 3
print("In", num_steps, "steps Drunk 3 moves", distance(drunk), "pixels.")

# exit on close window
turtle.exitonclick()
