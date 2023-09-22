def eh_quadrada(matriz):
    '''essa funcao retorna se a matriz dada como entrada Ã© quadrada
    True se sim, False se nÃ£o'''
    indice = 0
    if len(matriz) == 1:
        return True
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