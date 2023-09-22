def filtraMultiplos(lista,n):
    l = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo] % n ==0:
            l = l + (lista[proximo],)
        proximo = proximo + 1
    return l