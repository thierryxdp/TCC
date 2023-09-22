# Questão 3
def media_matriz(matriz):
    s = 0.
    c = 0
    for i in matriz:
        for j in i:
            s += j
            c += 1
    media = s/c
    return round(media, 2)