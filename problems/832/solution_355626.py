def eh_quadrada(matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    if nlin == ncol:
        return True
    if nlin != ncol:
        return False
    if matriz == []:
        return True