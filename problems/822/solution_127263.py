def repetidos(numeros):
    i = 0
    r = 0
    while i < len(numeros):
        if numeros[i] == numeros[i + 1]:
            r = r + 1
        i = i + 1
    return r