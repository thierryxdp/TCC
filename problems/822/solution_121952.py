def repetidos(lista):
    i = 1
    repeticao = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            repeticao = repeticao + 1
        i = i + 1
    return repeticao