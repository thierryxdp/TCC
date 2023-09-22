def filtraMultiplos(lista,n):
    r = []
    for i in range(len(lista)):
        if lista[i] % n == 0:
            r.append(lista[i])
            r.sort()
    return r