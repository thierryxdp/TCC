def media_matriz(matriz):
    mean = []
    for i in matriz:
        for n in i:
            mean.append(n)
    return round((sum(mean)/len(mean)), 2)