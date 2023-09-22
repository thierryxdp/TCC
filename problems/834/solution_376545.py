def media_matriz(matriz):
    ''''''
    linhas = len(matriz)
    colunas = len(matriz[0])
    soma = 0
    for i in range(linhas):
            soma += sum(matriz[i])
    return round(soma/(colunas*linhas),2)