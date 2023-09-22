def filtraMultiplos(lista, n):
    multiplos = []
    for i in lista:
        if i % n == 0:
            multiplos.append(i)
    return multiplos