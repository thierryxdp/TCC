def repetidos(lista):
    indice = 0
    rep = 0
    while indice > len(lista):
        indice = indice + 1
        if lista[indice-1] == lista[indice]:
            rep = rep + 1
            return rep