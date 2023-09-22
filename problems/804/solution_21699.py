def filtra_pares(t):
    '''retorna uma nova tupla contendo apenas
    os elementos pares da tupla t original'''
    f = ()
    if t[0]%2 == 0:
        f = f + tuple(str(t[0]))
    if t[1]%2 == 0:
        f = f + tuple(str(t[1]))
    if t[2]%2 == 0:
        f = f + tuple(str(t[2]))
    if t[3]%2 == 0:
        f= f + tuple(str(t[3]))
    return f