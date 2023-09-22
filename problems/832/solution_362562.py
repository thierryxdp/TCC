def eh_quadrada(matriz):
    """
    Função que identifica se uma matriz é quadrada ou não, retornando um valor booleano
    list -> bool
    """
    
    for i in range(len(matriz)):
        if len(matriz) == 0:
            return True
        for j in range(len(matriz[0])):
            if len(matriz) == len(matriz[0]):
                return True
            else: 
                return False