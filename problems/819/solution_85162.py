def filtraMultiplos(lista, n):
    listaMult = []
    for k in lista:
        if k%n == 0:
            listaMult.append(k)
    return listaMult