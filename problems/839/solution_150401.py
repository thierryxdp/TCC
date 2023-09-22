import math

def carros(p,c):
    if c > 1 :
    	return math.ceil(p/5)
    else:
        return math.ceil(p/c)