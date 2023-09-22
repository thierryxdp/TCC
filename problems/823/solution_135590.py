def faltante(L):
    """recebe uma lista com N - 1 inteiros e retorna qual numero do intervalo
    1 a N nao esta nessa lista
    list -> int"""
    
    n = len(L)
    
    numeros = list(range(1, n + 1))
    
    i = 0
    
    while i < n:
        if  numeros[i] not in L:
            return numeros[i]
        
        i += 1