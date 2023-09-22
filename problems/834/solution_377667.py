def media_matriz(matriz):
    '''calcula a média de todos os elementos da matriz de 
    entrada; list -> float'''
    linhas = len(matriz)
    colunas = len(matriz[0])
    a = 0
    for i in range(linhas):
        for j in range(colunas):
            a += matriz[i][j]
    return a / (linhas * colunas)