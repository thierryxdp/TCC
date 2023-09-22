def media_matriz(matriz):
    '''dada uma matriz(matriz) de inteiros nao vazia, 
    retorna a media de todos os numeros da matriz;
    list -> float'''
    linha = len(matriz)
    coluna = len(matriz[0])
    qtd_numeros = linha*coluna
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            soma = soma + matriz[i][j]
    media = round((soma/qtd_numeros),2)
    return media