def filtra_pares(a):
    # uma tupla com 4 números retorna uma tupla somente de números pares
    x = tuple()
    if a[0]%2 == 0: x += (a[0],)
    if a[1]%2 == 0: x += (a[1],)
    if a[2]%2 == 0: x += (a[2],)
    if a[3]%2 == 0: x += (a[3],)
    return x