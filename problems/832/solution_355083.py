def eh_quadrada(matriz):
    '''retorna true caso a matriz inserida seja quadrada e false caso contrario
    lista -> bool'''
    if matriz == []:
        return True
    nlin = len(matriz)
    ncol = len(matriz[0])
    if nlin == ncol:
        return True
    else:
        return False