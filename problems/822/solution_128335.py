def repetidos(lista):
    repeticoes = 0
    i = 0
    for e in lista: 
        if e == (lista[i - 1]):
            repeticoes = repeticoes + 1
            i = i + 1 
    return repeticoes