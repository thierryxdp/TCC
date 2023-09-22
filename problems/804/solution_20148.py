def filtra_pares(tupla):
    

    e1, e2, e3, e4 = tupla
    pares = tuple()

    if e1 % 2 == 0:
        pares += (e1, )

    if e2 % 2 == 0:
        pares += (e2, )

    if e3 % 2 == 0:
        pares += (e3, )

    if e4 % 2 == 0:
        pares += (e4, )

    return pares