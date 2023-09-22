#Start your python function here
def filtra_pares (a,b,c,d):
    '''filtragem recebe uma tupla com quatro elementos inteiros e devolve os elementos pares da tupla original, na mesma ordem em que se encontravam.
    int,int,int,int--> int'''
    a1=(abs(a))%2
    b1=(abs(b))%2
    c1=(abs(c))%2
    d1=(abs(d))%2
    tuplafinal=()
    if a1==0:
        tuplafinal=tuplafinal+(a,)
    if b1==0:
        tuplafinal=tuplafinal+(b,)
    if c1==0:
        tuplafinal=tuplafinal+(c,)
    if d1==0:
        tuplafinal=tuplafinal+(d,)
    return tuplafinal