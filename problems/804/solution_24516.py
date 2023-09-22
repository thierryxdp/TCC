def filtra_pares( T ):
    l = list()
    if T[0] % 2 == 0:
        l.append(T[0])
    if T[1] % 2 == 0:
        l.append(T[1])
    if T[2] % 2 == 0:
        l.append(T[2])
    if T[3] % 2 == 0:
        l.append(T[3])
    return tuple(l)