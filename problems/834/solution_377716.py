def media_matriz(A):
    """ Essa função retorna a média dos números da matriz.
    matriz ->int"""
    num_linhas_A, num_colunas_A = len(A),len(A[0])
    contador = 0
    for i in range(num_linhas_A):
        A[i][i] = i
        contador = contador + i
        media = contador/len(A)
    return media