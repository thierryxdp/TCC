def media_matriz (matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    total_numeros = linhas*colunas 
    total = 0
    for i in range(linhas):
        for j in range(colunas):
            total += matriz[i][j]
    média = total/total_numeros
    return f"{média:.2f}"