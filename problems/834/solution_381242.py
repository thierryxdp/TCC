import math
def media_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    s=0
    for x in range(linhas):
        s=s+sum(matriz[x])
    media = s/(linhas*colunas)
    return math.ceil(media*100)/100