def faltante(numeros):
    numeros.sort()
    i = 1
    if numeros[0] != 1:
        return 1
    elif i == len(numeros):
        return 2
    while i < len(numeros):
        if numeros[i] != numeros[i - 1] + 1:
            return numeros[i] - 1
        i = i + 1
    return numeros[i-1] + 1