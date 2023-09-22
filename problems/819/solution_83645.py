def filtraMultiplos(lista, n):
    listaDivisores = []
    for i in lista:
        if (i % n == 0):
            listaDivisores.append(i)
    return listaDivisores