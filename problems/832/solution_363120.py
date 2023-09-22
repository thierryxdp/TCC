def eh_quadrada(matriz):
    '''
    	Funcao que recebe uma matriz e identifica se e 
        quadrada
        list -> bool
    '''
    for linha in len(matriz):
        if linha == 0:
            return True
        for coluna in len(matriz[0]):
            if linha == coluna:
                return True