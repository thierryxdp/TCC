def eh_quadrada(matriz):
    """Funcao retorna um booleano que diz se a matriz dada: matriz e
    quadrada """
	
    if matriz == [[]]:
        return True
    elif matriz == []:
        return True
    else:
        i = len(matriz)
    	j = len(matriz[0])
        return i == j