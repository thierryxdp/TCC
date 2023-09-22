def eh_quadrada(matriz):
    '''Identifica se uma matriz é quadrada.
    int -> bool'''
    for i in range(0,len(matriz)):
        for j in range(0, len(matriz[i])):
            if len(matriz) == len(matriz[i]):
                return True
            else:
                return False
    if range(len(matriz)) == []:
    	return True