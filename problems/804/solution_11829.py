def filtra_pares (a):
    """função que filtra os números pares de uma tupla """
    """int, int, int, int -> int"""
    b = ()
    if ((a[0])%2) == 0:
        return a[0]
    if ((a[1])%2) == 0:
        return a[1]
    if ((a[2])%2) == 0:
        return a[2]
    if ((a[3])%2) == 0:
        return a[3]
    else:
        return ()