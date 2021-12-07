import random

def createDrunks(width, height):
    colorList = ['red', 'green', 'blue', 'black', 'purple', 'teal', 'yellow']
    ballColor = random.choice(colorList)
    speed = 0
    xcord = random.randint(-width/2, width/2)
    ycord = random.randint(-height/2, height/2)
    return [ballColor, speed, xcord, ycord]

