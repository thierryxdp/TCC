def repetidos(lista):
    x = 0
    y = 0
    z = y - 1
    while y < len(lista):
        if lista[y] == lista[z]:
            x = x + 1
        y = y + 1
    return x