def eh_quadrada(matriz):
    '''Função que identifica se uma matriz é quadrada
    list -> bool
    '''
    m = 0 
    
    for numero in matriz:
        if len(numero) == len(matriz):
            m += 1

    if m == len(matriz):
        return True
    else:
        return False