def media_matriz(matriz: list):
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    numeros = 0
    
    for i in range(linhas):
        for j in range(colunas):
            numeros += matriz[i][j]
            
    return numeros / (linhas * colunas)