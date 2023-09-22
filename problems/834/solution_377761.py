def media_matriz(m):
    soma, numeros = 0,0
    for i in range(len(m)):
        for j in range(len(m[i])):
            soma = soma + m[i][j]
            numeros = numeros + 1
	media = soma / numeros
    return round(media,2)