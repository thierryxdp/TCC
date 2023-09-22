def repetidos(lista):
    p = 1
    c = 0
    while p < len(lista):
        if lista[p] == lista[p-1]:
            c = c + 1
        p = p + 1
    return c