def media_matriz(m):
    numeros = []
    soma = 0
    for x in range(len(m)):
        for y in range(len(m[x])):
            list.append(numeros, m[x][y])
    for z in range(len(numeros)):
        soma = soma + numeros[z]
    media = soma/len(numeros)
    return round(media, 2)