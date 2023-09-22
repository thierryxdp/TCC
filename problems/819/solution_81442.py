def filtraMultiplos (lista,n):
    E = len(lista)
    R = []
    C = 0 
    while E > C:
        if lista [C]%n == 0:
            R += [lista[C],]
        C += 1
    return R