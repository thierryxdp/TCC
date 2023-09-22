def filtra_pares(a):
    '''Filtra os numeros pares de uma tupla com 4 elementos
    tupla(int, int, int, int) --> tupla(int, int, int, int)'''
    if((a[0]%2) == 0):
        p = 1
    else: p = 0
    if((a[1]%2) == 0):
        q = 1
    else: q = 0
    if((a[2]%2) == 0):
        r = 1
    else: r = 0
    if((a[3]%2) == 0):
        s = 1
    else: s = 0

    if((p == 1) and (q == 1) and (r == 1) and (s == 1)):
        return a
    if((p != 1) and (q == 1) and (r == 1) and (s == 1)):
        return a[1:]
    if((p != 1) and (q != 1) and (r == 1) and (s == 1)):
        return a[2:]
    if((p != 1) and (q != 1) and (r != 1) and (s == 1)):
        return a[3:]
    if((p != 1) and (q != 1) and (r != 1) and (s != 1)):
        return a[4:]
    if((p == 1) and (q != 1) and (r != 1) and (s != 1)):
        return a[:1]
    if((p != 1) and (q == 1) and (r != 1) and (s != 1)):
        return a[1:2]
    if((p != 1) and (q != 1) and (r == 1) and (s != 1)):
        return a[2:3]
    if((p == 1) and (q == 1) and (r != 1) and (s != 1)):
        return a[0:2]
    if((p != 1) and (q == 1) and (r == 1) and (s != 1)):
        return a[1:3]
    if((p == 1) and (q != 1) and (r != 1) and (s == 1)):
        return a[::2]
    if((p == 1) and (q != 1) and (r == 1) and (s != 1)):
        return a[:3:1]
    if((p != 1) and (q == 1) and (r != 1) and (s == 1)):
        return a[1::1]
    if((p == 1) and (q != 1) and (r == 1) and (s == 1)):
        return a[0]+a[2:]
    if((p == 1) and (q == 1) and (r != 1) and (s == 1)):
        return a[0:2]+a[3]
    if((p == 1) and (q == 1) and (r == 1) and (s != 1)):
        return a[0:3]