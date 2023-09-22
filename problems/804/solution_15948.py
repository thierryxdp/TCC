def filtra_pares(x):
    tupla = ()
    for y in range(1, 4):
        if x[y] % 2 == 0:
            tupla = tupla + x[y]
    return tupla