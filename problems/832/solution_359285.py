def eh_quadrada(matriz):
    ''' função que verifica se a matriz de entrada é ou não é quadrada;
    list -> bool '''
    i = len(matriz)
    j = len(matriz[0])
    if not matriz:
        return True
    if i == j:
        return True
	else:
        return False