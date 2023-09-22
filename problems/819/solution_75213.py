def filtraMultiplos(lista, n):
    divisores = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            divisores = divisores + [lista[proximo]]
        proximo = proximo + 1
    return divisores