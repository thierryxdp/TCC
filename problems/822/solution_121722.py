def repetidos(lista):
    proximo = 0
    repetições = 0
    while proximo<len(lista):
        if lista[proximo-1] == lista[proximo]:
            repetições = repetições + 1
        proximo = proximo + 1
    return repetições