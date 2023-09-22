def filtra_pares (tup):
    if tup[0] % 2 == 0 and tup[3] % 2 == 0:
        return (tup[0], tup[3])
    if tup[0] % 2 == 0 and tup[2] % 2 == 0 and tup[3] % 2 == 0:
        return (tup[0], tup[2], tup[3]