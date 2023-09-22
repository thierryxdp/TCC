def filtraMultiplos(lista,n):
    proximo = 0
    multiplos = []
    while proximo < len(lista):
        if lista[proximo]%n==0:
            multiplos = multiplos + (lista[proximos],)
        proximo = proximo + 1
    return multiplos