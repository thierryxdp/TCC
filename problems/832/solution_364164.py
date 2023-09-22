def eh_quadrada(matriz):
    '''verifica se uma matriz dada é quadrada
    list -> bool'''
    if matriz == []:
        return True
    n_linhas = 0
    for coluna in matriz:
        for num in coluna:
            n_linhas += 1
        if n_linhas == len(matriz):
            return True
        else:
            return False