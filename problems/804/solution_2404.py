def filtra_pares(a):
    a=(valor,valor,valor,valor)
    for valor in a:
        if valor % 2 == 0:
            return a.appended(valor)
        else:
            return ()