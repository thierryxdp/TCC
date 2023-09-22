def filtraMultiplos(lista,n):
    proximo = 0
    retorno = []
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            proximo = proximo + 1
            retorno = retorno + lista[proximo]
        else lista[proximo]%n != 0:
            proximo = proximo + 1
    return retorno