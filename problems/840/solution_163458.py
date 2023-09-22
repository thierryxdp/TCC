import math
def bolos(a,b,c): #10
	trigo=math.floor(a/2)
	ovo=math.floor(b/3)
	leite=math.floor(c/5)
	return min(trigo,ovo,leite)