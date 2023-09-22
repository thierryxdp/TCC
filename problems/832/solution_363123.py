def eh_quadrada(matriz):
    '''
    	Funcao que recebe uma matriz e identifica se e 
        quadrada
        list -> bool
    '''
    if len(matriz) == 0:
        return True
    for i in matriz:
        if len(i) == len(matriz):
            return True
        else:
            return False