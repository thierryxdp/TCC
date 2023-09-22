def repetidos(numeros):
    i = 0
    repetidos = 0
    while i < len(numeros):
        if numeros[i + 1] == numeros[i]:
            repetidos = repetidos + 1
        i = i + 1
    return repetidos