def filtraMultiplos(lista,num):
    multiplos = list()
    for c in lista:
        if c % num == 0:
            multiplos.append(c)
    return multiplos