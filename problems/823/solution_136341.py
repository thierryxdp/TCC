def faltante(numeros):
    numeros.sort()
    i = 0
    while i < len(numeros):
        if numeros[i] != numeros[i - 1] + 1:
            return numeros[i] -1
        i = i + 1
    return []