def filtraMultiplos(l,n):
    i=0
    filtra = []
    while i < len(l):
        if (l[i] % n) == 0:
            list.append(filtra, l[i])
        i = i + 1
    return filtra