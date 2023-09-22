def media_matriz(matriz):
    linha = len(matriz)
    coluna = len (matriz[0])
    soma = 0
    for i in range(linha):
        for j in range(coluna):
            elemento = matriz [i][j]
            soma = soma + elemento
    return round((soma/ (linha*coluna)),2)