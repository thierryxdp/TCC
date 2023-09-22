def filtraMultiplos(lista, n):
    filtrado = []
    for x in lista:
        if x % n ==0:
            filtrado.append(x)
    return filtrado