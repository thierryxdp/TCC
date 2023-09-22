def filtraMultiplos(lista,n):
    proximo = 0
    retorno = []
    while proximo < len(lista):
        if lista[proximo]%n == 0:
            list.append(retorno, lista[proximo])
            proximo = proximo + 1
        elif lista[proximo]%n != 0:
            proximo = proximo + 1
    return retorno