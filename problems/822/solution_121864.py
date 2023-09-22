def repetidos(lista):
    vezes = 0
    proximo = 0
    while proximo<len(lista):
        if (lista[proximo+1])==(lista[proximo]):
            vezes = vezes + 1
        proximo = proximo + 1
    return vezes