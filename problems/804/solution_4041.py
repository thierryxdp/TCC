def filtra_pares(t): 

    n1, n2, n3, n4 = None

    if t[0] % 2 != 0:
        n1 = t[0]

    elif t[1] % 2 != 0:
        n2 = t[1]

    elif t[2] % 2 != 0:
        n3 = t[2]

    elif t[3] % 2 != 0:
        n4 = [3]

    elemPares = (n1, n2, n3, n4)
    return elemPares