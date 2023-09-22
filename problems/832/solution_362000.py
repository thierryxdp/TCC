def eh_quadrada(m):
    nlin = len(m)
    ncol = len(m[0])
    if nlin == 0 or nlin == ncol:
        return True
    else:
        return False