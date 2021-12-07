import random

def createDrunks(width, height):
    colorList = ['red', 'green', 'blue', 'black', 'purple', 'teal', 'yellow']
    shapes = ['turtle', 'circle', 'square', 'triangle', 'classic']
    ballColor = random.choice(colorList)
    speed = 0
    xcord = random.randint(-width/2, width/2)
    ycord = random.randint(-height/2, height/2)
    shape = random.choice(shapes)
    pencolor = random.choice(colorList)
    return [ballColor, speed, xcord, ycord, shape, pencolor]

