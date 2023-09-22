def filtra_pares(tuplo):
    pares = tuple(it for it in tuplo if it[1]%2 == 0)
    impares = tuple(it for it in tuplo if it[1]%2 == 1)

    return (pares)#Start your python function here