def filtra_pares(a):
    '''Filtra os numeros pares de uma tupla com 4 elementos
    tupla(int, int, int, int) --> tupla(int, int, int, int)'''
    a1 = a[0]
    a2 = a[1]
    a3 = a[2]
    a4 = a[3]
    
    if((a1%2) == 0):
        p = 1
    else: p = 0
    if((a2%2) == 0):
        q = 1
    else: q = 0
    if((a3%2) == 0):
        r = 1
    else: r = 0
    if((a4%2) == 0):
        s = 1
    else: s = 0

    if((p == 1) and (q == 1) and (r == 1) and (s == 1)):
        return a1,a2,a3,a4
    if((p != 1) and (q == 1) and (r == 1) and (s == 1)):
        return a2,a3,a4
    if((p != 1) and (q != 1) and (r == 1) and (s == 1)):
        return a3,a4
    if((p != 1) and (q != 1) and (r != 1) and (s == 1)):
        return (a4,)
    if((p != 1) and (q != 1) and (r != 1) and (s != 1)):
        return ()
    if((p == 1) and (q != 1) and (r != 1) and (s != 1)):
        return (a1,)
    if((p != 1) and (q == 1) and (r != 1) and (s != 1)):
        return (a2,)
    if((p != 1) and (q != 1) and (r == 1) and (s != 1)):
        return a3,
    if((p == 1) and (q == 1) and (r != 1) and (s != 1)):
        return a1,a2
    if((p != 1) and (q == 1) and (r == 1) and (s != 1)):
        return a2,a3
    if((p == 1) and (q != 1) and (r != 1) and (s == 1)):
        return a1,a4
    if((p == 1) and (q != 1) and (r == 1) and (s != 1)):
        return a1,a3
    if((p != 1) and (q == 1) and (r != 1) and (s == 1)):
        return a2,a4
    if((p == 1) and (q != 1) and (r == 1) and (s == 1)):
        return a1,a3,a4
    if((p == 1) and (q == 1) and (r != 1) and (s == 1)):
        return a1,a2,a4
    if((p == 1) and (q == 1) and (r == 1) and (s != 1)):
        return a1,a2,a3