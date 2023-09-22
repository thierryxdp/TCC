def eh_quadrada(m):
    nlin = len(m)
    if nlin > 0:
        ncol = len(m[0])
        if ncol == nlin:
            return True
        else:
            return False
    
    return True