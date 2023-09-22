def filtra_pares(x):
    """recebe uma tupla(x) com 4 valores inteiros e devolve uma tupla com os valores pares na mesma ordem da tupla original tup->tup"""
    pares=()
    a,b,c,d=x
    if a%2==0:
        pares=pares+(a,)
    if b%2==0:
        pares=pares+(b,)
    if c%2==0:
        pares=pares+(c,)
    if d%2==0:
        pares=pares+(d,)
    return pares