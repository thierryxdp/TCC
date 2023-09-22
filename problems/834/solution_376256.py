def media_matriz(matriz):

    c=0
    soma=0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            c+=1
            print(c)
            soma+=sum(matriz[i])
            print(soma)
            media = soma/c

    return round(media,2)