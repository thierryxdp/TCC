def filtra_pares(x):
    tup = ()
    for y in x:
        if y//2 == 0:
            tup = tup+y
    return tup