def media_matriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            soma = soma + m[i][j]
            numeros = numeros + 1
	media = soma / numeros
    return round(media,2)