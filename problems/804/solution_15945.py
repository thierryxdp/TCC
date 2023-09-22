def filtra_pares(x):
    tupla = ()
    for y in x:
        if y % 2 == 0:
            tupla = tupla +x[y]
    return tupla