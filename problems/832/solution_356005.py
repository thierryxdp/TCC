def eh_quadrada (matriz):
    '''Identifica se a matriz inserida é uma matriz quadrada e retorna "True" ou "False" em relação a tal identificação;
    list -> bool'''
    colunas = len(matriz[0])
    linhas = len(matriz)
    if linhas == colunas:
        return True
    else:
        return False