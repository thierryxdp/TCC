def filtra_pares(k):
    """recebe uma tupla com quatro elementos e retorna uma nova contendo elementos pares."""
    k2=()
    a=k[0]
    b=k[1]
    c=k[2]
    d=k[3]
    if a%2==0:
        k2=k2+(a,)
    if b%2==0:
        k2=k2+(b,)
    if c%2==0:
        k2=k2+(c,)
    if d%2==0:
        k2=k2+(d,)
        return tuple(k2)