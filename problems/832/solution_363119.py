def eh_quadrada(matriz):
    '''
    	Funcao que recebe uma matriz e identifica se e 
        quadrada
        list -> bool
    '''
    for linha in len(matriz):
        if len(matriz) == 0:
            return True
        for coluna in len(matriz[0]):
            if len(matriz) == len(matriz[0]):
                return True