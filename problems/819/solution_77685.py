def filtraMultiplos(lista,num):
    multiplos = list()
    for x in lista:
        if x % num == 0:
            multiplos.append(x)
    return multiplos