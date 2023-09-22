def repetidos(lista):
    repeticoes = 0
    l = 0
    for e in lista:
        if  e == (lista[i - l]):
            repeticoes = repeticoes + 1
            i = i + l
        else:
            repeticoes = repeticoes
            i = i + l
    return repeticoes