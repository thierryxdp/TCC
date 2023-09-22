def filtra_pares(t):
    """Retornar uma tupla t de quatro elementos somente com os seus elementos pares; int->int"""
    pares = ()
    proximo = 0
    if t[proximo]%2==0:
        pares= pares+ (t[proximo],)
    proximo = proximo + 1
    if t[proximo]%2==0:
        pares= pares+ (t[proximo],)
    proximo = proximo + 1
    if t[proximo]%2==0:
        pares= pares+ (t[proximo],)
    proximo = proximo + 1
    if t[proximo]%2==0:
        pares= pares+ (t[proximo],)
    return pares