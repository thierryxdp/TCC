def media_matriz(matriz):
    lista = []
    linhas = len(matriz)
    colunas = len (matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            lista = lista + matriz
    return lista