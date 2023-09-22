def media_matriz(m):
    """A função retorna a média de todos os números da matriz.
       list -> float"""
    media = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            list.appen(media, m[i][j])
    return round(sum(media)/len(media), 2)