def filtraMultiplos (lista, n):
    a = lista[:]
    if a% n == 0:
    return a
    else:
        return []