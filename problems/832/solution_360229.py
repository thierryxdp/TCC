def eh_quadrada(matriz):
    
    if not matriz:
		return True
    
    nlin = len(matriz)
    ncol = len(matriz[0])

    for i in range(len(matriz)):
        if not len(matriz[i]) == nlin:
            return False

    for j in range(len(matriz[0])):
        if not len(matriz[j]) == ncol:
            return False

    return True