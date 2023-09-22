def eh_quadrada(matriz):
    '''Retorna se uma matriz é ou não quadrada
    list --> bool'''
    if matriz == []:
        return True
    return len(matriz) == len(matriz[0])