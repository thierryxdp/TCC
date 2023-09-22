def eh_quadrada(matriz):
    '''Função que identifica se a matriz dada como entrada é
    	uma matriz quadrada. list --> bool.'''
    linhas = len(matriz)
    if len (matriz)==0:
        return True
    colunas = len(matriz[0])
    return coluna ==linhas