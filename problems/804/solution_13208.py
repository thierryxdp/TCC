def filtra_pares(t):
    for t[1] in t:
        if t[1] % 2 == 0:
            return t[1]
    for t[2] in t:
        if t[2] % 2 == 0:
            return t[2]