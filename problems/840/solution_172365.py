import math
def bolos(a,b,c):
    farinha = a/2
    ovos =b /3
    leite = c/5
    if farinha == ovos and farinha == leite :
       return farinha 
	else :
        resp = min(farinha,ovos,leite)
        return math.floor(resp)