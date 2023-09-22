def media_matriz(matriz):
    """Recebe uma matriz e retorna a média de todos os seus valores.
    	list -> float"""
    
    quant = 0
    soma = 0
    
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
    		soma += matriz[i][j]
    		quant += 1
    
    return soma/quant