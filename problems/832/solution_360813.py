def eh_quadrada(matriz):
    linha=len(matriz)
    coluna=len(matriz[0])
    if linha>1:
    	if linha == coluna:
        	return True
    	else:
        	return False
    else:
        False