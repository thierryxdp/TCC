def filtra_pares (x):
    '''filtragem recebe uma tupla com quatro elementos inteiros e devolve os elementos pares da tupla original, na mesma ordem em que se encontravam.
    int,int,int,int--> int'''
    x0=(abs(x[0]))%2
    x1=(abs(x[1]))%2
    x2=(abs(x[2]))%2
    x3=(abs(x[3]))%2
    tuplafinal=()
    if x0==0:
        tuplafinal=tuplafinal+(x[0],)
    if x1==0:
        tuplafinal=tuplafinal+(x[1],)
    if x2==0:
        tuplafinal=tuplafinal+(x[2],)
    if x3==0:
        tuplafinal=tuplafinal+(x[3],)
    return tuplafinal