def media_matriz(matriz):
    soma=0
    total=0
    for i in range(len(m)):
        for j in range(len(matriz[0])):
            total=total+1
            soma=soma+matriz[i][j]
    media=soma/total
    return round(media,2)