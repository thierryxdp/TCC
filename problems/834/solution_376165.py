def media_matriz(lista):
    total = 0
    qntd = 0
    media = 0
    for i in len(lista):
        for j in len(lista[0]):
            total = total + lista[i][j]
    qntd = i*j
    media = total / qntd
    return round(2, media)