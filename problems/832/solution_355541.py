def eh_quadrada(m):
    '''
    Esta função recebe uma matriz como parametro e retorna um valor booleano informado se a matriz dada
    é quadrada ou não.
    
    Parametros
    ----------
    m (list) : matriz
    
    Observações
    -----------
    Matriz deve ser informada como lista de listas
    '''
    if len(m) == 0:
        return True
    else:
    	return len(m) == len(m[0])