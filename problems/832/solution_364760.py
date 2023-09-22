def eh_quadrada(M):
    nlin = len(M)
    ncol = len (M[0])
    if nlin == ncol:
        return True
    if nlin != ncol:
        return False