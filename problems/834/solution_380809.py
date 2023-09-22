def media_matriz(matriz, n):
    matriz = []
    linha=len(m1)
    coluna= len(m1[0])
    linha=coluna
    for i in range(linha):
        matriz.append([])
        for j in range(coluna):
            resultado = m1[i][j] + m2[i][j] / n
            matriz[i].append(resultado)
    return matriz