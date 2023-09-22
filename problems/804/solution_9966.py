def filtra_pares(M):
    """filtra os números pares de uma tupla M
    tuple->tuple"""
    a, b, c, d = M
    A = a % 2
    B = b % 2
    C = c % 2
    D = d % 2
    if A == 0 and B == 0 and C == 0 and D == 0:
        return (a,b,c,d)
    elif A == 0 and B == 0 and C == 0:
        return (a,b,c)
    elif A == 0 and B == 0 and D == 0:
        return (a,b,d)
    elif A == 0 and C == 0 and D == 0:
        return (a,c,d)
    elif B == 0 and C == 0 and D == 0:
        return (b,c,d)
    elif A == 0 and B == 0:
        return (a,b)
    elif A == 0 and C == 0:
        return (a,c)
    elif A == 0 and D == 0:
        return (a,d)
    elif B == 0 and C == 0:
        return (b,c)
    elif B == 0 and D == 0:
        return (b,d)
    elif C == 0 and D == 0:
        return (c,d)
    elif A == 0:
        return (a,)
    elif B == 0:
        return (b,)
    elif C == 0:
        return (c,)
    elif D == 0:
        return (d,)
    else:
        return ()