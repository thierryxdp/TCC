def eh_quadrada(matriz):
    linha = len(matriz[0])
    coluna=len(matriz)
    if linha==coluna:
        return True
    elif matriz == []:
    	return True
    else:
        return False