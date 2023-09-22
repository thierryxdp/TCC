def filtra_pares(x):
    tupla = ()
    for y in range(0, 3):
        if x[y] % 2 == 0:
            tupla = tupla + x[y]
    return tupla