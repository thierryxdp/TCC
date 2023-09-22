def media_matriz(matriz):
    """ Calcula a média de todos os números da matriz.
    	list -> float
        
        Parameter:
        matriz: Matriz.
        
        Returns:
        A média de todos os números da matriz.
    """
    soma = 0
    for i in matriz:
        for j in i:
            soma = soma + j
    return soma / (j+i)