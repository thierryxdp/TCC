def media_matriz(m):
    soma = 0 
    elementos = len(m)*len(m[0])
    for i in range(len(m)):
        for j in range(len(m[0])):
            soma = soma + m[i][j]
    media = soma/elementos
    return round(media,2)