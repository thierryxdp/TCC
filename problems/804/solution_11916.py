def filtra_pares (a):
    """função que filtra os números pares de uma tupla """
    """int, int, int, int -> int"""
    b = (a)
    if ((a[0])%2) == 0:
        return a[0]
    elif ((a[1])%2) == 0:
        return a[1]
    elif ((a[2])%2) == 0:
        return a[2]
    elif ((a[3])%2) == 0:
        return a[3]
    else:
        return ()