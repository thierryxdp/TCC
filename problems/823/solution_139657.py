def faltante(lista):
    i = 0
    c = 0
    while i< len(lista):
        if lista[i] not in range(0,len(lista)):
            c = c +lista[i]
        i = i + 1
    return c