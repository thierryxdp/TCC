def eh_quadrada(matriz):
    '''essa funcao retorna se a matriz dada como entrada é quadrada
    True se sim, False se não'''
    linhas = len(matriz)
    if len(matriz[0]) == 0: 
        return True
    else:
        pass
    colunas = len(matriz[0])
    if linhas == colunas:
        return True
    elif linhas == 0:
        return True
    else:
        return False