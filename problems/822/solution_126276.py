def repetidos(lista):
    i = 0
    repetido = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            repetido = repetido + 1
        if i == len(lista):
            return repetido
        i = i + 1