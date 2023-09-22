def repetidos(numeros):
    k = 0
    i = 0
    j = i - 1
    while i in range(len(numeros)):
        if numeros[i] == numeros[j]:
            k = k + 1
        i = i + 1
        j = j + 1
    return k