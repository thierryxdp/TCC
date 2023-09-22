def filtra_pares(t):
    """recebe uma tuple e filtra seus numeros pares
    tuple -> tuple"""
    a,b,c,d = t
    x = []
    if a%2 == 0 :
        list.append(x,a)
    if b%2 == 0 :
        list.append(x,b)
    if c%2 == 0 :
        list.append(x,c)
    if d%2 == 0 :
        list.append(x,d)
    return tuple(l)