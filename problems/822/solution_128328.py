def repetidos(lista):
    repeticoes = 0
    for e in lista:
        repeticoes = repeticoes + 1
        if (lista[e-1]) == (lista[e]):
        return repeticoes