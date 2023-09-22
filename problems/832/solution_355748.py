def eh_quadrada(matriz):
    ''' função que avalia a matriz dada como entrada,
        classificando-a como quadrada ou não
        [list-->bool]'''

    if matriz == []:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False