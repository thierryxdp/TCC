def filtra_pares(x):
    """Dado uma tupla com quatro elementos inteiros,
    retorna uma nova tupla contendo somente os elementos pares da tupla.
    tuple --> tuple"""
    a,b,c,d = x
    L=()
    if a%2==0:
        L=L+ (a,)
    if b%2==0:
        L=L+(b,)
    if c%2==0:
        L=L+(c,)
    if d%2==0:
        L=L+(d,)
    return L