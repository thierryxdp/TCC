def repetidos(lista):
    i = 0
    c = 0
    x = 999999999999
    while i < len(lista):
        if lista[i] > 0:
            if lista[i] == x:
                c = c+1
        x = lista[i]
        i = i + 1
    return c