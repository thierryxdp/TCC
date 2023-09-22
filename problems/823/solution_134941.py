def faltante(n):
    '''Dada uma lista com inteiros repetidos de 1 à N,
    a função retorna o numero faltante nesse intervalo
    '''
    
    indice=0
    
    while indice<len(n):
        if indice+1 not in (n):
            return indice+1
        indice=indice+1
    return indice+1