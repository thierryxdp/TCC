def melhor_volta(matriz):
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    minimo = []
    for i in range(nlinhas):
        for j in range(ncolunas):
            minimo.append(matriz[i][j])
            if matriz[i][j] == min(minimo):
                corredor = i + 1
                volta = j + 1
                resultado = matriz[i][j]
    return (corredor,resultado,volta)