import math

def bolos(a,b,c):
    f=(a/2)
    o=(b/3)
    l=(c/5)
	if (f<o) and (f<l):
    	return f
	elif (o<f) and (o<l):
    	return o
	else:
    	return l