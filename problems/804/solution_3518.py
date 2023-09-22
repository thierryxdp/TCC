def filtra_pares(lista):
    """ """
    a, b, c, d = lista
    a1 = a%2
    b1 = b%2
    c1 = c%2
    d1 = d%2
    if a1 == 0 and b1 == 0 and c1 == 0 and d1 == 0:
        return (a,b,c,d)
    elif a1 == 0 and b1 == 0 and c1 == 0 and d1 != 0:
        return (a, b, c)
    elif a1 == 0 and b1 == 0 and c1 != 0 and d1 == 0:
        return (a, b,d)
    elif a1 == 0 and b1 != 0 and c1 == 0 and d1 == 0:
        return (a,c,d)
    elif a1 != 0 and b1 == 0 and c1 == 0 and d1 == 0:
        return (b,c,d)
    elif a1 == 0 and b1 == 0 and c1 != 0 and d1 != 0:
        return (a, b)
    elif a1 == 0 and b1 != 0 and c1 == 0 and d1 != 0:
        return (a, c)
    elif a1 != 0 and b1 == 0 and c1 == 0 and d1 != 0:
        return (b,c)
    elif a1 == 0 and b1 != 0 and c1 != 0 and d1 == 0:
        return (a, d)
    elif a1 != 0 and b1 != 0 and c1 == 0 and d1 == 0:
        return (c,d)
    elif a1 != 0 and b1 == 0 and c1 != 0 and d1 == 0:
        return (b,d)
    elif a1 != 0 and b1 != 0 and c1 != 0 and d1 == 0:
        return (d,)
    elif a1 != 0 and b1 != 0 and c1 == 0 and d1 != 0:
        return (c,)
    elif a1 != 0 and b1 == 0 and c1 != 0 and d1 != 0:
        return (b,)
    elif a1 == 0 and b1 != 0 and c1 != 0 and d1 != 0:
        return (a,)
    else:
        return ()