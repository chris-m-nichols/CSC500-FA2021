import math

def distance(x1, x2, y1, y2):
    x = x1-x2
    y = y1-y2
    dist = math.sqrt(x**2 + y**2)
    return dist
