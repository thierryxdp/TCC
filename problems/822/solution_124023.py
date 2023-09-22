def repetidos(lista):
    i = 0
    n = 0
    while i<len(lista):
        if lista[i]=lista[1+i]:
            n = n + 1
        i = i + 1
    return n