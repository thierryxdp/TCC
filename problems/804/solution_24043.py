def filtra_pares(t):
    ''' filtra os elementos pares de uma tupla t'''
    if t[0]%2 == 0:
        a = t[0]
    if t[1]%2 == 0:
        b = t[1]
    if t[2]%2 == 0:
        c = t[2]
    if t[3]%2 == 0:
        d = t[3]
    n = (a,b,c,d)
    return n