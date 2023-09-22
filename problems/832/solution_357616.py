def eh_quadrada(matriz):
    '''verifica se uma raiz é quadrada, usando a função len para
    para saber o tamanho da string nessa caso o tamano da matriz.'''
    if len(matriz)==0:
    	return True
    for c in matriz:
        if len(matriz)!=len(c):
            return False
    else:
         return True