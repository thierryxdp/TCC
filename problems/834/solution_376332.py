def media_matriz(matriz):
    """ """
    total = 0
    quantidade = 0
    media = 0 
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total+= matriz[i][j]
            quantidade+= 1
    media = total/ quantidade
    return round(media,2)