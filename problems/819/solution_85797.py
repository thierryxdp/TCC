def filtraMultiplos(numeros,n):
    multiplos = ()
    proximo = 0
    while proximo < len(numeros):
    if numeros[proximo]%2 == 0:
        multiplos = multiplos + (numeros[proximo],)
        proximo = proximo + 1
        return multiplos