#Filtragem
def filtra_pares(t):
    '''Esta função retorna uma nova tupla apenas com os valores
    pares de uma tupla dada.
    int, int, int, int -> int'''
    a=t[0]
    b=t[1]
    c=t[2]
    d=t[3]
    k=()
    if a%2==0:
        k=(a,)
    if b%2==0:
        k=k+(b,)
    if c%2==0:
        k=k+(c,)
    if d%2==0:
        k=k+(d,)
    return k