def media_matriz(Matriz):
    media = 0
    for i in len(Matriz):
        for j in len(Matriz[0]):
            media += Matriz[i][j]
    media=media/len(Matriz)
    return round(media,2)