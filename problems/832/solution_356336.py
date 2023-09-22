def eh_quadrada(matriz):
    '''indetifica se é uma matriz quadrada. list(list)->boolean'''
    if len(matriz) == 0:
        return True
    for z in matriz:
        if len(matriz) != len(z):
            return False
        else:
            return True