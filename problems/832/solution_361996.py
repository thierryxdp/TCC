def eh_quadrada(matriz):
    '''A funcao identifica se uma matriz é quadrada
    list->bool'''
    if matriz==[]:
        return True
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False