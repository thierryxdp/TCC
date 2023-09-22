def filtra_pares(x):
    pares = ()
    index = len(x)
    i=0
    lista = []
    while i < index:
        if x[i] % 2 == 0:
            lista.append(x[i])
            i=+1
            return pares