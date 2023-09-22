def repetidos(numeros):
    soma = 0
    for c in numeros:
        if numeros.index(c) == numeros.index(c-1):
            soma += 1
    return soma