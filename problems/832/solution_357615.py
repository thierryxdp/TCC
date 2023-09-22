def eh_quadrada(matriz):
    '''verifica se uma raiz é quadrada
    list(list)->boolean'''
    if len(matriz)==0:
    	return True
    for c in matriz:
        if len(matriz)!=len(c):
            return False
    else:
         return True