def eh_quadrada(matriz):
    if matriz==[]:
        return True
    else:
        linha=len(matriz)
    	coluna=len(matriz[0])
    	if linha==coluna:
        	return True
    	else:
        	return False