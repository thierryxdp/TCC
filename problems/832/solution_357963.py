def eh_quadrada(matriz):
    """Identifica se uma matriz é quadrada
    	list -> bool
        Parameters:
        matriz: Matriz a ser identificada
        
        Returns:
        Se a matriz é quadrada ou não
    """
    
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if len(matriz) == len(matriz[i]) and len(matriz[j]):
                return True
            else:
                return False
    return True