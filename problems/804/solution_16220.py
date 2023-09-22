def filtra_pares(a):
    """recebe uma tupla com quatro elementos e retorna uma nova contendo elementos pares."""
    a2=()
    a=a[0]
    b=a[1]
    c=a[2]
    d=a[3]
    if a%2==0:
        a2=a2+(a,)
    if b%2==0:
        a2=a2+(b,)
    if c%2==0:
        a2=a2+(c,)
    if d%2==0:
        a2=a2+(d,)
        return tuple(a2)