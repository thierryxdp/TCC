def eh_quadrada(matriz):
    '''Função que recebe uma matriz e identifica se ela é quadrada
    	ou não, retornando True caso seja e False caso não seja
        
        list(list) -> bool'''
    
    if matriz == []:
        return True
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False