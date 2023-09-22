def repetidos(lista):
    x = 0
    y = 0
    while y < len(lista):
        if lista[x] == lista[(x-1)]:
            x = x + 1
        y = y + 1
    return x