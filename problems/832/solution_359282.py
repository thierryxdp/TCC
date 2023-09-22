def eh_quadrada(matriz):
    ''' ffunção que verifica se a matriz de entrada é ou não é quadrada;
    list -> bool '''
    i = len(matriz)
    j = len(matriz[0])
    if i == j:
        return True
	else:
        return False