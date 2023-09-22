def repetidos(lista):
    c = 0
    d = 0
    for x in lista:
        if lista[c] == lista[c-1]:
            d += 1
        c += 1
    return d