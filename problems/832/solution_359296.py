def eh_quadrada(matriz):
    '''identifica se uma matriz é quadrada
    list[ list ] -> boolean'''
    if matriz == []:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        False