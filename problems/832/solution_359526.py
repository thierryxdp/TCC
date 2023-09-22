def eh_quadrada(matriz):
    '''identifica se a matriz dada é quadrada ou não.
    matriz -> bool'''
    linhas = len(matriz)
    if linhas == 0:
        return True
    colunas = len(matriz[0])
    if linhas == colunas:
        return True
    else:
        return False