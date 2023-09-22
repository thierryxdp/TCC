def media_matriz(matriz: list):
    """ dada uma matriz, no formato lista e de números inteiros não vazia,
    retorna a média de todos os números da matriz, com exatamente duas casas
    decimais de precisão """
    
    linhas = len(matriz)
    colunas = len(matriz[0])
    
    numeros = 0
    
    for i in range(linhas):
        for j in range(colunas):
            numeros += matriz[i][j]
            
    return round(numeros / (linhas * colunas), 2)