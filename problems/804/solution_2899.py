def filtra_pares(t):
    """
    Função que filtra apenas os valores pares de uma tupla com 4 elementos.
    """
    t0=t[0]
    t1=t[1]
    t2=t[2]
    t3=t[3]
    pares=()
    if t0/2==t0//2:
        pares=pares+(t0,)
    if t1/2==t1//2:
        pares=pares+(t1,)
    if t2/2==t2//2:
        pares=pares+(t2,)
    if t3/2==t3//2:
        pares=pares+(t3,)
    return pares