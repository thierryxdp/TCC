def repetidos(lista):
    repeticoes = 0
    i = 0
    for e in lista: 
        if (lista[e - 1]) == (lista[e]):
            repeticoes = repeticoes + 1
            i = i + 1
        return repeticoes