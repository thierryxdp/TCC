def bolos(a,b,c):
    farinha = a/2
    ovos =b /3
    leite = c/5
    if farinha == ovos and farinha == leite :
       return farinha 
	else :
        return min(farinha,ovos,leite)