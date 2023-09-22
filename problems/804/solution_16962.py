def filtra_pares(t):
    """Retornar uma tupla t de quatro elementos somente com os seus elementos pares; int->int"""
    pares = ()
    if t[0]%2==0:
        pares= pares+ (t[0],)
    elif t[1]%2==0:
        pares= pares+ (t[1],)
    elif t[2]%2==0:
        pares = pares+ (t[2],)
    elif t[3]%==0:
        pares = pares+ (t[3],)
    return pares