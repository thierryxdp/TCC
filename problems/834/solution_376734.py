def media_matriz(matriz):
    '''Calcula a média (com duas casas decimais de 
    precisão) de todos os número de uma
    matriz de números inteiros não vazia;
    list -> float'''
    
    soma = 0
    linhas = len(matriz)
    colunas = len(matriz[0])
    qtd = linhas * colunas
    
    for i in range(linhas):
        for j in range(colunas):
            soma += matriz[i][j]
    
    return soma/qtd