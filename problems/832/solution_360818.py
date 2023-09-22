def eh_quadrada(matriz):
    linha=len(matriz)
    coluna=len(matriz[0])
    if linha==0 and coluna==0:
        return True
    else:
    	if linha==coluna:
        	return True
    	else:
        	return False