def repetidos(lista):
    repeticoes = 0
    i = 0
    for e in lista:
        if  e == (lista[i-l]):
            repeticoes = repeticoes + 1
            i = i + 1
        else:
            repeticoes = repeticoes
            i = i + 1
    return repeticoes