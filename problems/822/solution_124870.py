def repetidos(numeros):
    indice = 1
    contador = 0
    while indice < len(numeros):
        if numeros[indice] == numeros[indice-1]:
            contador += 1
        indice += 1
    return contador