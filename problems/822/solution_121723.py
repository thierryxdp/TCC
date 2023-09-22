def repetidos(lista):
    proximo = 0
    repeticoes = 0
    while proximo<len(lista):
        if lista[proximo-1] == lista[proximo]:
            repeticoes = repeticoes + 1
        proximo = proximo + 1
    return repeticoes