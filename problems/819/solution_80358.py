def filtraMultiplos(lis, n):
    lista = list()
    for c in len(lis):
        if c%n==0:
            lista.append(c)
    return lista