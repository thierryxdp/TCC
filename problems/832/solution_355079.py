def eh_quadrada(matriz):
    '''retorna true caso a matriz inserida seja quadrada e false caso contrario
    lista -> bool'''
    nlin = len(matriz)
    ncol = len(matriz[0])
    if nlin == ncol:
        return True
    elif nlin == 1 and ncol == 0:
            return True
    else:
        return False