def filtra_pares(a,b,c,d):
    '''filtra números pares da tupla; int, int, int, int->tuple'''
    if(a%2==0):
        return a
    if(b%2==0):
        return b
    if(c%2==0):
        return c
    if(d%2==0):
        return d
    tuple(a,b,c,d)