def eh_quadrada(matriz):
    '''Retorna se uma matriz é quadrada, uma matriz 
    vazia é considerada quadrada
    	list -> bol'''
    return not (len(matriz) and len(matriz) != len(matriz[0]))