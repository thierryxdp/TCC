def eh_quadrada(m):
    nlin = len(m)
    ncol = len(m[0])
    if nlin == ncol:
        return True
    elif m == []:
        return True
    else:
        return False