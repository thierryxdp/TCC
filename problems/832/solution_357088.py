def eh_quadrada(matriz):
    '''essa funcao retorna se a matriz dada como entrada é quadrada
    True se sim, False se não'''
    linhas = len(matriz)
    colunas = len(linhas[0])
    if linhas == colunas:
        return True
    if linhas == 0:
        return True
    else:
        return False