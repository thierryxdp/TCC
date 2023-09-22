def filtraMultiplos(lista, n):
    lis = []
    nprox = 0
    while nprox<len(lista):
        if (lista[nprox])%n == 0:
            lis = lis + (lista[nprox],)
        nprox = nprox + 1
    return lis