def faltante(numeros):
    numeros.sort()
    i = 0
    while i < len(numeros):
        if i+1 != numeros[i]:
            return i+1
        i = i + 1
    return i+1