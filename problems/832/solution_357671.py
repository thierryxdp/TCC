def eh_quadrada(matriz):
    '''essa funcao retorna se a matriz dada como entrada é quadrada
    True se sim, False se não'''
    indice = 0
    while indice < len(matriz):
        linhas = len(matriz)
        colunas = len(matriz[0])
        if linhas == colunas:
            return True
        elif linhas == 0:
            return True
        elif colunas == 0:
            return True
        else:
            return False
    return True