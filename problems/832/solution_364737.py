def eh_quadrada(matriz):
    if matriz == []:
    	return True
    linha = len(matriz[0])
    coluna=len(matriz)
   
    if linha==coluna:
        return True
    
    else:
        return False