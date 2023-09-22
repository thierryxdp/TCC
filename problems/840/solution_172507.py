import math
def bolos(t, o , l):
	x=math.floor(t/2)
    y=math.floor(o/3)
    z=math.floor(l/3)
   
	if x<=y and x<=z:
        return x
    elif y<=x and y<=z:
        return y
    else:
        return z