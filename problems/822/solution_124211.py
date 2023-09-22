def repetidos(lista):
    k = 0
    for i in range(lista):
        if lista[i] == lista[i-1]:
            k += 1
    return k