def filtra_pares(numeros):
    """recebe uma tupla com 4 numeros inteiros e retorna um tupla com os que, entre esses, 
    sao pares"""
    
    return tuple(x for x in numeros if (it % 2 == 0))