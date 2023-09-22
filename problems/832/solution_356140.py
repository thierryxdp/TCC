def eh_quadrada(matriz):
    '''Retorna se a matriz de entrada é quadrada ou não.
    matrix->bool'''
    if len(matriz)==0:
        return True
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False