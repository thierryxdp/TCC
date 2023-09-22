def eh_quadrada(matriz):
    '''Essa função identifica se uma matriz é quadrada;
    list->bool'''
    if len(matriz)==0:
    	return True
    linha=matriz[0]
    numero_colunas=len(linha)
    numero_linhas=len(matriz)
    if numero_colunas==numero_linhas:
    	return True
    return False