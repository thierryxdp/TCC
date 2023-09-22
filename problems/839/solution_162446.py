import math

def carros (p, c=5):
    if p%5==0:
        return p/5
    elif p/c!=0:
        return math.ceil(p/c)