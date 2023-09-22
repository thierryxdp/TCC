def eh_quadrada(m):
    if m == []:
        return True
    nlin = len(m)
    ncol = len(m[0])
    if nlin == ncol:
        return True
    else: 
        return False