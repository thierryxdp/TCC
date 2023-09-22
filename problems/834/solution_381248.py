import math
def media_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    s=0
    for x in range(linhas):
        s=s+sum(matriz[x])
    m=s/(linhas*colunas)
    if math.ceil(m)-m > m-math.floor(m):
        return math.floor(m*100)/100
    elif math.ceil(m)-m < m-math.floor(m):
        return math.ceil(m*100)/100
    else:
        return m