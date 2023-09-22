import math

def carros(p,c):
    if c is not 0 :
    	return math.ceil(p/c)
    else:
        return math.ceil(p/5)