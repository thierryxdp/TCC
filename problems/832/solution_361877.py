def eh_quadrada(matriz):
    '''
    	Funcao recebe uma matriz e verifica se ela
        é ou nao quadrada, se for, retorna True, caso
        contrario, retorna false.
        list -> bool
        
    '''
    if matriz == []:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return false