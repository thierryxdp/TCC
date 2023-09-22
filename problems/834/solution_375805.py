def media_matriz(matriz):
    '''calcula a média de todos os números de uma matriz de inteiros não vazia;
    list(list) -> float'''
    linhas = len(matriz)
    colunas = len(matriz[0])
    elementos = linhas * colunas
    total = 0
    for i in matriz:
        for j in i:
            total += j
    return round((total/elementos),2)