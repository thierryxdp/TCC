def repetidos(numeros):
    soma = 0
    for c in numeros:
        if numeros[numeros.index(c)] == numeros[numeros.index(c)-1]:
            soma =soma + 1
    return soma