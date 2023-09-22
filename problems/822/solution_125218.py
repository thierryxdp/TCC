def repetidos(lista):
    i=1
    repeticoes = 0
    while i<len(lista):
        if lista[i-1]==lista[i]:
            repeticoes = repeticoes+1
    i = i+1
    return repeticoes