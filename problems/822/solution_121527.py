def repetidos (lista):
    i = 0
    n = 0
    while i > 1 and i < len(lista):
        if lista[i] == lista[i-1]:
            n = n + 1
        i = i + 1
    return n