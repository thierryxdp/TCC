def filtra_pares(a):
    """recebe uma tupla com quatro elementos e retorna uma nova contendo elementos pares."""
    a2=()
    a=a2[0]
    b=a2[1]
    c=a2[2]
    d=a2[3]
    if a%2==0:
        a2=a2+(a,)
    if b%2==0:
        a2=a2+(b,)
    if c%2==0:
        a2=a2+(c,)
    if d%2==0:
        a2=a2+(d,)
        return tuple(a2)