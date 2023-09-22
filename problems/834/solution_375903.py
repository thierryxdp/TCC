def media_matriz(matriz):
    """dada uma matriz de inteiros não vazia, a função retorna a média de todos os números da matriz com exatamente duas
    casas decimais de precisão; list -> float"""
    linhas = len(matriz)
    colunas = len(matriz[0])
    soma = 0
    
    for i in range(linhas):
        for j in range(colunas):
            soma += matriz[i][j]
            
    media = soma/(linhas*colunas)
    
    return round(media, 2)