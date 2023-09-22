def repetidos(lista):
    vezes = 0
    proximo = 0
    while proximo<len(lista):
        if (lista[proximo])==(lista[proximo-1]):
            vezes = vezes + 1
        proximo = proximo + 1
    return vezes