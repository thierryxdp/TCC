def eh_quadrada (matriz):
    '''Identifica se a matriz inserida é uma matriz quadrada e retorna "True" ou "False" em relação a tal identificação;
    list -> bool'''
    linhas = len(matriz)
    if linhas == 0:
        return True
    colunas = len(matriz[0])
    if linhas == colunas:
        return True
    else:
        return False