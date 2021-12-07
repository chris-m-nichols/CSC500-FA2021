# Bouncing Balls Simulation Program

import turtle
import random
from createDrunks import createDrunks

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
    if drunk.get_xCor() < -screen_width / 2:
        print(drunk.get_xCor())
        return True
    else:
        print(drunk.get_xCor())
        return False

def atRightEdge(drunk, screen_width):
    if drunk.get_xCor() > screen_width / 2:
        return True
    else:
        return False

def atTopEdge(drunk, screen_height):
    if drunk.get_xCor() > screen_height / 2:
        return True
    else:
        return False

def atBottomEdge(drunk, screen_height):
    if drunk.get_yCor() < -screen_height / 2:
        return True
    else:
        return False

# Randomize directions
# change to change direction, update with random direction based on instructions

def change_position(drunk, stepSize,width,height):
    DIRECTIONS = [0,45, 90, 135, 180, 225, 270, 315]
    if atLeftEdge(drunk,width):
        DIRECTIONS.remove(225) 
        DIRECTIONS.remove(270)
        DIRECTIONS.remove(315)     
    elif atRightEdge(drunk,width): 
        DIRECTIONS.remove(0)
        DIRECTIONS.remove(45)
        DIRECTIONS.remove(90)
    elif atBottomEdge(drunk,height): 
        DIRECTIONS.remove(135)
        DIRECTIONS.remove(180)
        DIRECTIONS.remove(225)
    elif atTopEdge(drunk,height):
        DIRECTIONS.remove(0)
        DIRECTIONS.remove(45)
        DIRECTIONS.remove(315)

    drunk.turtle.setheading(random.choice(DIRECTIONS))
    drunk.turtle.forward(stepSize)


        

# Calculate Distance

def distance(drunk):
    dist = drunk.turtle.distance(drunk.get_startxcor(),drunk.get_startycor())   
    return dist
    
    
    
#Create Drunkards
#change
# ---- main
# program greeting
print('This program simulates drunkards walk in a turtle screen')
print('for a specified number of steps.')

# init screen size
screen_width = 1000
screen_height = 800
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
    change_position(drunk1, stepSize,screen_width,screen_height)
for k in range(num_steps):
    change_position(drunk2, stepSize,screen_width,screen_height)
for k in range(num_steps):
    change_position(drunk3, stepSize,screen_width,screen_height)

# add equation for distance from start point
#Math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

print("In", num_steps, "steps Drunk 1 moves", distance(drunk1))
print("In", num_steps, "steps Drunk 2 moves", distance(drunk2))
print("In", num_steps, "steps Drunk 3 moves", distance(drunk3))

# exit on close window
turtle.exitonclick()
