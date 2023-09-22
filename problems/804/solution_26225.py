def filtra_pares(tup):
    pares = ()
    contador = 0
    while contador < len(tup):
        pares = pares + (tup[contador],)
        contador = contador + 1
    return pares