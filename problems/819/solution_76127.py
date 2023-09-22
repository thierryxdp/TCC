def filtraMultiplos(lista,numero):
    Multiplos = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            Multiplos = Multiplos + t[proximo]
        proximo = proximo + 1
    return Multiplos