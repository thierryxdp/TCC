def eh_quadrada(matriz):
    linha = len(matriz[0])
    coluna=len(matriz)
    if matriz == []:
    	return True
    if linha==coluna:
        return True
    
    else:
        return False