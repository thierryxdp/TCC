def eh_quadrada(matriz):
    '''Dada uma matriz qualquer, retorna True, caso esta
    matriz seja quadrada, e False, caso contrário.
    list -> bool'''
    if matriz == [] or len(matriz) == len(matriz[0]):
        return True
    else:
        return False