def eh_quadrada(matriz):
    '''funcao que identifica se a matriz dada na entrada é quadrada ou não;
    list->bool'''
	if matriz == []:
        return True
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if len(matriz) == len(matriz[l]):
                return True
            else:
                return False