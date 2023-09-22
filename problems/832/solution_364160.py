def eh_quadrada(matriz):
    '''verifica se uma matriz dada é quadrada
    list -> bool'''
    if matriz == '':
        return True
    n_colunas = 0
    n_linhas = 0
    for coluna in matriz:
        n_colunas += 1
        for linha in coluna:
            n_linhas += 1
    if n_colunas == n_linhas:
        return True
    else:
        return False