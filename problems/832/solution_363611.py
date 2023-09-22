def eh_quadrada(matriz):
    '''Recebe uma matriz e identifica se a matriz é quadrada ou não.
    list -> bool'''
    soma = []
    
    for i in matriz:
    	for j in i:
        	if len(matriz[0]) == len(matriz[0][1]):
                return True
            else:
                return False