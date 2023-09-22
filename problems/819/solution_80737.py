def filtraMultiplos(lista,n):
    i = 0
    multiplos = []
    while lista[i] <= len(lista):
        if lista[i] % n == 0:
            multiplos += [lista[i]]
        i += 1
    return multiplos