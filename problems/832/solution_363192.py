def eh_quadrada(matriz):
    '''Funcao identifica se a matriz é quadrada, ou seja,
    se a quantidade de linhas é igual de colunas;list->bool'''
    if len(matriz)==0:
        return True
    for i in matriz:
        if len(matriz)==len(matriz[0]):
            return True
        else:
            return False