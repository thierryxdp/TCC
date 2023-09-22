def repetidos(lista):
    """ """
    indice = 0
    proximo = 1
    vezes = 0
    while proximo < len(lista):
        if lista[proximo] == lista[indice]:
            vezes += 1
        indice += 1
        proximo += 1
    return vezes