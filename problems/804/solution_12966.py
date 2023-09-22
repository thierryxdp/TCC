def filtra_pares(numeros):
    """recebe uma tupla com 4 numeros inteiros e retorna os que, entre esses, sao pares"""
  
    for i in numeros:
        if (i % 2 == 0):
            return numeros[i]