def media_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    s=0
    for x in range(linhas):
        s=s+sum(matriz[x])
    return round((s/(linhas*colunas)),2)