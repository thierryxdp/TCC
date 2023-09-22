def media_matriz(matriz):
    """..."""
    
    soma = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma = soma + matriz[i][j]
    return soma