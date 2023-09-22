def faltante(L):
    """recebe uma lista com N - 1 inteiros e retorna qual numero do intervalo
    1 a N nao esta nessa lista
    list -> int"""
    
  	n = len(L) + 1
    
    numeros = list(range(1, n))
    
    i = 0
    
    while i < len(numeros):
        if  numeros[i] not in L:
            return numeros[i]
        
        i += 1