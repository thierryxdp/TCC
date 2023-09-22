def eh_quadrada(matriz):
    """Funcao retorna um booleano que diz se a matriz dada: matriz e
    quadrada """
	
    if matriz == [[]]:
        return True
    
    i = len(matriz)
    j = len(matriz[0])

    if matriz == []:
        return True
    else:
        return i == j