def media_matriz(lista):
    total = 0
    qntd = 0
    media = 0
    for i in range(len(lista)):
        for j in range(len(lista[0])):
            total = total + lista[i][j]
    qntd = max.i*max.j
    media = total / qntd
    return round(2, media)