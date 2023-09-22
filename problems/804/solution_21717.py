def filtra_pares(t):
    '''retorna uma nova tupla contendo apenas
    os elementos pares da tupla t original'''
    f = ()
    def par(x):
        if x%2 ==0:
            return (x,)
        else:
            return False
    if par(t[0]):
        f = par(t[0])
    if par(t[1]):
        f = f + par(t[1])
    if par(t[2]):
        f = f + par(t[2])
    if par(t[3]):
        f = f + par(t[3])
    return f