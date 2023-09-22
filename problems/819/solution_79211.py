def filtraMultiplos(lista, n):
    i = 0
    newlist = []
    while i < len(lista):
        if lista[i]%n == 0:
            list.append(newlist, lista[i])
        i += 1
    return newlist