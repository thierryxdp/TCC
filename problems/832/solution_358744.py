def eh_quadrada(matriz):
    '''Função que identifica se a matriz dada como entrada é
    	uma matriz quadrada. list --> bool.'''
    linhas = len(matriz)
    colunas = len(matriz[0])
    if len (matriz)==0:
        return True
    return coluna ==linhas