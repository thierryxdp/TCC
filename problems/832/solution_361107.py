def eh_quadrada(matriz):
    """
    Essa função recebe uma matriz e retorna se ela é quadrada ou não;
    list -> bool
    """
    if matriz == []:
        return True
    nlin = len(matriz)
    ncol = len(matriz[0])
    if nlin == ncol:
        return True
    return False