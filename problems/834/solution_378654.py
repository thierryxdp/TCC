def media_matriz(matriz):
    '''Função que recebe uma matriz de inteiros não vazia e retorna
    a média de todos os valores da matriz
    list -> int'''
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])
    numero_de_termos = n_linhas*n_colunas
    soma = 0
    for i in range(n_linhas):
        for j in range(n_colunas):
            soma = soma + matriz[i][j]
    media = soma/numero_de_termos
    return media