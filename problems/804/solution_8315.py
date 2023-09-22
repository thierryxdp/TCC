def filtra_pares(t):
    """retorna uma tupla com todos os elementos pares de uma tupla original (t) de quatro elementos inteiros.
       tupla -> tupla"""
    pares = ()
    if t[0]%2 == 0:
        pares = pares + (t[0],)
    if t[1]%2 == 0:
        pares = pares + (t[1],)
    if t[2]%2 == 0:
        pares = pares + (t[2],)
    if t[3]%2 == 0:
        pares = pares + (t[3],)
    return pares