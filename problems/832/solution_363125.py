def eh_quadrada(matriz):
    '''Função que identifica se uma matriz é quadrada
    list -> bool
    '''
    m = 0 
    
    for numero in matriz_q:
        if len(numero) == len(matriz_q):
            m += 1

    if m == len(matriz_q):
        return True
    else:
        return False