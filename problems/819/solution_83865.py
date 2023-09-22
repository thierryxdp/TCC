def filtraMultiplos(lista,n):
    numeros = ()
    proximo = 0

    while proximo < len(lista):
        if lista[proximo]%n == 0:
            numeros +=  (lista[proximo],)
        proximo = proximo +1
    return list(numeros)