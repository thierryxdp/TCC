def eh_quadrada (m):
    """funcao que analisa se uma matriz m inserida e quadrada ou nao

       lista->bool
    """

    nlin= len(m)
    ncol= len(m[0])

    if nlin == ncol:
        return True

    elif nlin != ncol:
        return False
    
    else:
        return True