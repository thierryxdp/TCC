def eh_quadrada(matriz):
    '''Retorna se a matriz de
    entrada e ou nao quadrada
    list --> bool'''
    if matriz == []:
        return True
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False