def media_matriz(matrix):
    '''função que dada uma matriz de entrada, retorna a
    média de todos os seus valores com precisão de 2 casas 
    decimais; list -> float'''
    accumulator = 0
    n_linhas = len(matrix)
    n_colunas = len(matriz[0])
    for i in range(n_linhas):
        for j in range(n_colunas):
            accumulator += matriz[i][j]
            a = accumulator/ n_colunas * n_linas
            return a