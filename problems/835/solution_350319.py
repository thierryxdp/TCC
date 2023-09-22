def melhor_volta(matriz):
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    minimo = min(min(matriz))
    for i in range(nlinhas):
        for j in range(ncolunas):
            if matriz[i][j] == minimo:
                corredor = i + 1
                volta = j + 1 
    return (corredor,minimo,volta)