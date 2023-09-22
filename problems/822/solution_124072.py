def repetidos(lista):
    i = 0
    n = 0
    while i<len(lista):
        i = i + 1
        if lista[i-1]==lista[i]:
            n = n + 1
    return n