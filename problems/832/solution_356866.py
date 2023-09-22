def eh_quadrada(matriz):
    for i in range (len(matriz)):
    	if len(matriz)==len(matriz[i]):
        	return True
    if matriz == []:
        return True
    else: 
        return False