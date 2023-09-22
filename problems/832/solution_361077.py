def eh_quadrada(matriz):
    nlin = len(matriz)
    ncol = len(matriz[0])
    if nlin == 0:
        return True
    elif nlin == ncol :
        return True
    elif nlin != ncol:
        return False