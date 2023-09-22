def filtraMultiplos(numeros,n):
    multiplos = []
    proximo = 0
    while proximo <len(numeros):
        if numeros[proximo]%n == 0:
            multiplos = multiplos.append(numeros[proximo])
        proximo = proximo + 1
        return multiplos