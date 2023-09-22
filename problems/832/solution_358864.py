def eh_quadrada(matriz):
    '''Função que identifica se a matriz dada como entrada é
    	uma matriz quadrada. list --> bool.'''
    if len (matriz)==0:
        return True
        linhas=len(matriz)
        colunas=len(matriz[0])
    	return  colunas==linhas