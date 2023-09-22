import math
def bolos(a,b,c): #10
	trigo=math.ceil(a/2)
	ovo=math.ceil(b/3)
	leite=math.ceil(c/5)
	return min(trigo,ovo,leite)