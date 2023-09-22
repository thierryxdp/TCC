def filtra_pares (x,y,z,w):
    '''filtragem recebe uma tupla com quatro elementos inteiros e devolve os elementos pares da tupla original, na mesma ordem em que se encontravam.
    int,int,int,int--> int'''
    x1=(abs(x))%2
    y1=(abs(y))%2
    z1=(abs(z))%2
    w1=(abs(w))%2
    tuplafinal=()
    if x1==0:
        tuplafinal=tuplafinal+(x,)
    if y1==0:
        tuplafinal=tuplafinal+(y,)
    if z1==0:
        tuplafinal=tuplafinal+(z,)
    if w1==0:
        tuplafinal=tuplafinal+(w,)
    return tuplafinal