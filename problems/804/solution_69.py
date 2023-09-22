def filtra_pares (a,b,c,d):
    '''filtragem recebe uma tupla com quatro elementos inteiros e devolve os elementos pares da tupla original, na mesma ordem em que se encontravam.
    int,int,int,int--> int'''
    a1=(abs(a))%2
    b1=(abs(b))%2
    c1=(abs(c))%2
    d1=(abs(d))%2
    tuplafinal()
    if a1==0:
        tuplafinal=tuplafinal+(a1,)
    if b1==0:
        tuplafinal=tuplafinal+(b1,)
    if c1==0:
        tuplafinal=tuplafinal+(c1,)
    if d1==0:
        tuplafinal=tuplafinal+(d1,)
    return tiplafinal