def repetidos(lista):
    i = 0
    n = 0
    lista1 = lista
    while i<len(lista):
        if lista[i]==lista1[i+1]:
            n = n + 1
        i = i + 1
    return n