def media_matriz(matriz):
    """dada uma matriz de inteiros não vazia,
retorna a média de todos os números da matriz"""
    nlin = len(matriz) #qnt de linha
    ncol = len(matriz[0]) #qnt de coluna
    soma = 0

    for i in range(nlin): 
        for j in range(ncol):
            soma += matriz[i][j] #soma todos elementos

    qnt = nlin*ncol #qnt de elementos da matriz
    media = soma/qnt  

    return round(media,2)