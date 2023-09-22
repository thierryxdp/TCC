def filtra_pares(tupla):
    for n in tupla:
        if tupla[n-1]%2 == 0:
            return n,
        else:
            return ()