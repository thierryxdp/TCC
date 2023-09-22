def filtraMultiplos(lista,numero):
    Multiplos = []
    proximo = 0
    while proximo < len(lista):
        if lista[proximo]%numero == 0:
            Multiplos = Multiplos + lista[proximo]
        proximo = proximo + 1
    return Multiplos