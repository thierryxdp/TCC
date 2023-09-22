def repetidos(lista):
    index = 0
    repeticoes = 0
    for item in lista:
        if index > 0:
            if item > lista[index-1]:
                repeticoes = repeticoes + 1
        index = index + 1

    return repeticoes