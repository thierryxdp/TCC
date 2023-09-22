def filtra_pares(t):
    ''' filtra os elementos pares de uma tupla t'''
    n = ()
    if t[0]%2 == 0:
        a = [t[0]]
        n0 = n + a
    else:
        n0 = n
    if t[1]%2 == 0:
        b = [t[1]]
        n1 = n0 + b
    else:
        n1 = n0
    if t[2]%2 == 0:
        c = [t[2]]
        n2 = n1 + c
    else:
        n2 = n1
    if t[3]%2 == 0:
        d = [t[3]]
        n3 = n2 + d
    else:
        n3 = n2
    return n3