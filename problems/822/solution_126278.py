def repetidos(lista):
    i = 0
    repetido = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            repetido += 1
        i = i + 1
    return repetido