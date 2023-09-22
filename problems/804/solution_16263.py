def filtra_pares(k):
    """recebe uma tupla com quatro elementos e retorna uma nova contendo elementos pares."""
    k1=()
    a=k[0]
    b=k[1]
    c=k[2]
    d=k[3]
    if a%2==0:
        k1=k1+(a,)
    if b%2==0:
        k1=k1+(b,)
    if c%2==0:
        k1=k1+(c,)
    if d%2==0:
        k1=k1+(d,)
        return tuple(k1)