import math
def carros(n,c= None):
    if c== None:
    	return math.ceil(n/5)
    else:
   	 	return math.ceil(n/c)