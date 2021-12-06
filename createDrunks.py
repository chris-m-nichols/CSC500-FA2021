import random

def createDrunks():
    colorList = ['red', 'green', 'blue', 'black', 'purple', 'teal', 'yellow']
    xcords = [-40, 0, 40]
    ycords = [-40, 0, 40]
    ballColor = random.choice(colorList)
    speed = 0
    xcord = random.choice(xcords)
    ycord = random.choice(ycords)
    return [ballColor, speed, xcord, ycord]

