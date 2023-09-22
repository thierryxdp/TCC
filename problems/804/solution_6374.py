def filtra_pares(t):
    """Função que calcula apenas os elementos pares da tupla original,
    tupla --> tupla"""
    tv = ()
    if t[0]%2 == 0:
        tv = tv + (t[0],)
    if t[1]%2 == 0:
        tv = tv + (t[1],)
    if t[2]%2 == 0:
        tv = tv + (t[2],)
    if t[3]%2 == 0:
        tv = tv + (t[3],)
    return tv