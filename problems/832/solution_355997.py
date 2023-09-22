def eh_quadrada (matriz):
    '''Identifica se a matriz inserida é uma matriz quadrada e retorna "True" ou "False" em relação a tal identificação;
    list -> bool'''
    linhas = len(matriz[0])
    colunas = len(matriz)
    if linhas == colunas:
        return True
    elif colunas and linhas = 0:
        return True
    else:
        return False