def filtra_pares(numeros):
    """recebe uma tupla com 4 numeros inteiros e retorna os que, entre esses, sao pares"""
    
    i = 0
    for i in numeros:
        if (i % 2 == 0):
            return numeros[i]
            i += 1
            
        else:
            i += 1