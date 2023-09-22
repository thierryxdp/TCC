def faltante(numeros):
    total = len(numeros) + 1
    numeros.sort()
    indice = 1
    while indice < total:
        if numeros[indice-1] != indice:
            return indice
        indice += 1
    return indice