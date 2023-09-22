def media_matriz(m):
    media = 0
    for i in range(len(m)):
        for j in range(len(m[0])):
            media = media + m[i][j]
    media = media / (i*j)
    return round(media,2)