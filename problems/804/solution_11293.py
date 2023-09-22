def filtra_pares([a,b,c,d]):
    '''retorna uma tupla apenas com os elementos pares da original
    (int,int,int,int) -> tupla com até 4 elementos'''
    if (a%2)==0:
        return a,
    if (b%2)==0:
        return b,
    if (c%2)==0:
        return c,
    if (d%2)==0:
        return d,
    else:
        return ()