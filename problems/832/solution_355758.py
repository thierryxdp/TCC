def eh_quadrada(matriz):
    '''função que verifica se a matriz é, de fato, quadrada.
    list->bool'''
    if matriz==[]:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False