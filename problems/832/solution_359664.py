def eh_quadrada(matriz):
    ''' Dado uma matriz, retorna se ela e quadrada ou nao,
    	matriz sem nenhuma linha ou coluna (vazia), e 
        considerada quadrada
        list -> str
     '''
	m = []
    if len(matriz) == len(matriz[0]):
        return True
    if matriz == m:
        return True
    else:
        return False