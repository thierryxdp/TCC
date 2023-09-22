def eh_quadrada(matriz):
    '''Verifica se uma matriz é quadrada
    list -> bool'''
    eh_quadrada = False
    if len(matriz) == 0:
        eh_quadrada = True
    else:
        if len(matriz) == len(matriz[0]):
            eh_quadrada = True
    return eh_quadrada