def repetidos(numeros):
    i = 1
    n = 0
    while i < len(numeros):
        if numeros[i] == numeros[i - 1]:
            n = n + 1
        i = i + 1
        return n