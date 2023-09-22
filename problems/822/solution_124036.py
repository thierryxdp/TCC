def repetidos(lista):
    i = 0
    n = 0
    while i<len(lista):
        lista1 = lista[i]
        if lista1==lista[i+1]:
            n = n + 1
        i = i + 1
    return n