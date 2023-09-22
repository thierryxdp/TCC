def media_matriz(matriz):
    m1=matriz
    linha=len(m1)
    coluna= len(m1[0])
    n=linha*coluna
    linha=coluna
    for i in range(linha):
        matriz.append([])
        for j in range(coluna):
            resultado = m1[i][j] + m2[i][j] / n
    return resultado