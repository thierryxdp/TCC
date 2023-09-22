def eh_quadrada(matriz):
    '''verifica se uma matriz é quadrada
    list(list)->boolean'''
    if len(matriz) == 0:
        return True
    for i in matriz:
        if len(i) != len(matriz[0]):
            return False
    return True