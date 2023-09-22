def media_matriz(matriz):
    c=0
    s=0
    media=[]
    for s in range(len(matriz)):
        for c in range(len(matriz[s])):
            media.append(matriz[s][c])
            s2 = (sum(media)/len(media))
    return round(s2,2)