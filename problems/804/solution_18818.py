def filtra_pares(t):
    '''Filtra os numeros pares de uma tupla
    tupla[int, int, int, int] --> tupla(int, int, int, int)'''
    a = t[0]
    b = t[1]
    c = t[2]
    d = t[3]
    
    if((a%2) == 0):
        p = 1
    else: p = 0
    if((b%2) == 0):
        q = 1
    else: q = 0
    if((c%2) == 0):
        r = 1
    else: r = 0
    if((d%2) == 0):
        s = 1
    else: s = 0

    if((p == 1) and (q == 1) and (r == 1) and (s == 1)):
        return a,b,c,d
    if((p != 1) and (q == 1) and (r == 1) and (s == 1)):
        return b,c,d
    if((p != 1) and (q != 1) and (r == 1) and (s == 1)):
        return c,d
    if((p != 1) and (q != 1) and (r != 1) and (s == 1)):
        return (d,)
    if((p != 1) and (q != 1) and (r != 1) and (s != 1)):
        return ()
    if((p == 1) and (q != 1) and (r != 1) and (s != 1)):
        return (a,)
    if((p != 1) and (q == 1) and (r != 1) and (s != 1)):
        return (b,)
    if((p != 1) and (q != 1) and (r == 1) and (s != 1)):
        return c,
    if((p == 1) and (q == 1) and (r != 1) and (s != 1)):
        return a,b
    if((p != 1) and (q == 1) and (r == 1) and (s != 1)):
        return b,c
    if((p == 1) and (q != 1) and (r != 1) and (s == 1)):
        return a,d
    if((p == 1) and (q != 1) and (r == 1) and (s != 1)):
        return a,c
    if((p != 1) and (q == 1) and (r != 1) and (s == 1)):
        return b,d
    if((p == 1) and (q != 1) and (r == 1) and (s == 1)):
        return a,c,d
    if((p == 1) and (q == 1) and (r != 1) and (s == 1)):
        return a,b,d
    if((p == 1) and (q == 1) and (r == 1) and (s != 1)):
        return a,b,c