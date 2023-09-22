import math

def bolos (A,B,C):
	a= math.ceil(A/2)
    b= math.ceil(B/3)
    c= math.ceil (C/5)
    return min(a,b,c)