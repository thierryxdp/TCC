def eh_quadrada(matriz):
    '''Dada uma matriz, retorna True se for quadrada e False se não for.
    list -> bool'''
    if matriz == []:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False