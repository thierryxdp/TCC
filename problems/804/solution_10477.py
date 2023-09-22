def filtra_pares(tupla):
    """recebe uma tupla com 4 valores e retorna os termos pares. str->int"""
    A,B,C,D = tupla
    a = int(A)
    b = int(B)
    c = int(C)
    d = int(D)
    if (a%2 == 0):
        return (a)
    elif not(a%2==0):
        return ()
    elif (b%2==0):
        return (b)
    elif not(b%2==0):
        return ()
    elif (c%2==0):
        return (c)
    elif (not(c%2==0)):
        return ()
    elif (d%2==0):
        return (d)
    elif not(d%2==0):
        return ()
    
    return '('(a)+','+(b)+','(c)+','+(d)+')'