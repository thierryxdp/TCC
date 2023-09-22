def eh_quadrada(m):
    nlin = len(m)
    if nlin==0:
        return true
    else:
        ncol = len(m[0])
    
        if ncol==0:
            ncol=1
        if nlin == ncol:
            return True
        else:
            return False