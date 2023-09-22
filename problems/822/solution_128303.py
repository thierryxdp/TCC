def repetidos(numeros):
    repetidos = 0
    i = 1
    while i < len(numeros):
        if numeros[i] == numeros[i-1]:
            repetidos += 1
        i = i + 1
    return repetidos