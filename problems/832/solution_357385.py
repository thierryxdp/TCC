def eh_quadrada(matriz):
    '''Identifica se uma matriz é quadrada. Recebe a matriz(list) e retorna uma valor booleano(bool).'''
    linhas = len(matriz)
    colunas = len(matriz[0])
    if matriz == []:
        return True
    if linhas == colunas:
        return True
    else:
        return False