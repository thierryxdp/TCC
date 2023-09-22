def media_matriz(matriz):
    r = []
    for i in matriz:
        for j in i:
            r.append(j)
    return round(sum(r)/len(r), 2)