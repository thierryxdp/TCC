def eh_quadrada(matriz):
    '''essa funcao retorna se a matriz dada como entrada é quadrada
    True se sim, False se não'''
    linhas = len(matriz)
    colunas = len(matriz[0])
    if linhas == colunas:
        return True
    elif linhas == 0 and linhas == 1:
        return True
    else:
        return False