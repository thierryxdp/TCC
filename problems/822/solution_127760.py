def repetidos(lista):
    i = 0
    j = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            j += 1
            i += 1
        else:
            i += 1
    return j