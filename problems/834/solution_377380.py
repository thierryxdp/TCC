def media_matriz(matriz):
    i=0
    media=0
    while i<len(matriz):
        media=media+((sum(matriz[i]))/len(matriz[i]))
        return round(media,2)
        i=i+1