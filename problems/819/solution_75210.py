def filtraMultiplos(lista, n):
    divisores()
    proximo = 0
    while proximo < len(lista):
        if t[proximo]%n == 0:
            divisores = divisores + (t[proximo],)
        proximo = proximo + 1
    return divisores