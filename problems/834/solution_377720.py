def media_matriz(A):
    """ Essa função retorna a média dos números da matriz.
    matriz ->int"""
    num_linhas_A, num_colunas_A = len(A),len(A[0])
    novamatriz = []
    for i in range(num_linhas_A):
        for k in range(num_colunas_A):
            novamatriz[i][k] = A[i][k] + novamatriz[i][k]
            media = novamatriz//num_linhas_A
    return media