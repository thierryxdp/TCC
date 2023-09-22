def filtra_pares(t):
    """."""
    a = (t[0] % 2) == 0
    b = (t[1] % 2) == 0
    c = (t[2] % 2) == 0
    d = (t[3] % 2) == 0
    nova_tupla = (a,b,c,d)
    return nova_tupla