def eh_quadrada(matriz):
    if len(matriz)==0:
    	return True
    for c in matriz:
        if len(matriz)!=len(c[0]):
            return False
    else:
         return True