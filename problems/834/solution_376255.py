def media_matriz(matriz):

    c=0
    soma=0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            c+=1
            soma=sum(matriz[i])
            media = soma/c

    return round(media,2)