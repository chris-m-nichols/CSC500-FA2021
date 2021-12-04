# Bouncing Balls Simulation Program

import turtle
import random
import time


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
    for k in range(0, num_balls):
        new_ball = turtle.Turtle()
        new_ball.shape('circle')
        ballColor = random.choice(colorList)
        new_ball.fillcolor(ballColor)
        new_ball.speed(0)
        new_ball.penup()
        new_ball.setheading(random.randint(1,359))
        balls.append(new_ball)

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
num_balls = 3

# create balls
balls = createBalls(num_balls)

# set start time
#start_time = time.time()

# begin simulation
terminate = False

#update with number of moves

#Needs to be setting the direction 
def make_drunkard_walk(step_size,step_number):
    for i in range(step_size,step_number):
        turtle.setheading(90*random.randint(0,3))
        turtle.forward(step_size)

# add equation for distance from start point


# exit on close window
turtle.exitonclick()
