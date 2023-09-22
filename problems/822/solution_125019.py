def repetidos(lista):
    x = 0
    k = 1
    while k < len(lista):
        if lista[k] == lista[k-1]:
            x = x + 1
        k = k + 1
    return x