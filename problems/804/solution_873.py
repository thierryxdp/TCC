def filtra_pares(x,y,z,w):
    """Função em que dados quatro números naturais x,y,z,w retorna uma tupla contendo somente os que são pares.
    int, int, int, int -> int"""
    x%2 = i1
    y%2 = i2
    z%2 = i3
    w%2 = i4
    if (i1 and i2 and i3 and i4) == 0:
        return x,y,z,w
    if (i1 and i2 and i3) == 0 and i4 != 0:
        return x,y,z
    if (i1 and i2) == 0 and (i3 and i4) != 0:
        return x,y
    if i1 == 0 and (i2 and i3 and i4) =! 0:
        return x