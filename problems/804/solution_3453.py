def filtra_pares(a, b, c, d):
    """ essa função irá filtrar todos os números inteiros pares e recolocará em ordem dada pela tupla original 
    int, int, int, int -> tupla(int) """
    x1 = a%2
    x2 = b%2
    x3 = c%2
    x4 = d%2
    if x1 != 0:
        return (b, c, d)
    elif x2 != 0:
        return(a, c, d)
    elif x3 != 0:
        return (a, b, d)
    elif x4 != 0:
        return (a, b, c)
    elif x1 != 0 and x2 != 0:
        return (c, d)
    elif x2 != 0 and x3 != 0:
        return (a, d)
    elif x3 != 0 and x4 != 0:
        return (a, b)
    elif x1 != 0 and x4 != 0:
        return (b, c)
    elif x1 != 0 and x2 != 0 and x3 != 0:
        return (d)
    elif x2 != 0 and x3 != 0 and x4 != 0:
        return (a)
    elif x1 != 0 and x3 != 0 and x4 != 0:
        return (b)
    elif x1 != 0 and x2 != 0 and x4 != 0:
        return (c)
    else:
        return ()