def filtra_pares(x):
    """Função que receba uma tupla(a) com quatro elementos e retorne uma nova
    tupla contendo apenas os elementos pares da tupla original.
    tupla -> tupla"""
    
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    
    
    if((x[0]%2) == 0):
        p = 1
    else: p = 0
    if((x[1]%2) == 0):
        q = 1
    else: q = 0
    if((x[2]%2) == 0):
        r = 1
    else: r = 0
    if((x[3]%2) == 0):
        s = 1
    else: s = 0


    if((p == 1) and (q == 1) and (r == 1) and (s == 1)):
        return x1, x2, x3, x4
    if((p != 1) and (q == 1) and (r == 1) and (s == 1)):
        return x2, x3, x4
    if((p != 1) and (q != 1) and (r == 1) and (s == 1)):
        return x3, x4
    if((p != 1) and (q != 1) and (r != 1) and (s == 1)):
        return (x4,)
    if((p != 1) and (q != 1) and (r != 1) and (s != 1)):
        return ()
    if((p == 1) and (q != 1) and (r != 1) and (s != 1)):
        return (x1,)
    if((p != 1) and (q == 1) and (r != 1) and (s != 1)):
        return (x2,)
    if((p != 1) and (q != 1) and (r == 1) and (s != 1)):
        return (x3,)
    if((p == 1) and (q == 1) and (r != 1) and (s != 1)):
        return x1, x2
    if((p != 1) and (q == 1) and (r == 1) and (s != 1)):
        return x2, x3
    if((p == 1) and (q != 1) and (r != 1) and (s == 1)):
        return x1, x4
    if((p == 1) and (q != 1) and (r == 1) and (s != 1)):
        return x1, x3
    if((p != 1) and (q == 1) and (r != 1) and (s == 1)):
        return x2, x4
    if((p == 1) and (q != 1) and (r == 1) and (s == 1)):
        return x1, x3, x4
    if((p == 1) and (q == 1) and (r != 1) and (s == 1)):
        return x1, x2, x4
    if((p == 1) and (q == 1) and (r == 1) and (s != 1)):
        return x1, x2, x3