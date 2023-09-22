def repetidos(lista):
    quantidade = 0
    indice = 0
    while indice > 0 and indice < len(lista):
        if lista[indice+1] == lista[indice]:
            quantidade += 1
        indice += 1
    return quantidade