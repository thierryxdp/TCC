def repetidos(lista):
    repeticoes = 0
    s = [e for e in lista if ((lista[e-1]) == (lista[e]))]
    repeticoes = repeticoes + 1
    return s