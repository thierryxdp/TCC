def eh_quadrada(matriz):
    if matriz == []:
        return True
    nlin = len(matriz)
    ncol = len(matriz[0])
    if nlin == ncol:
        return True
    return False