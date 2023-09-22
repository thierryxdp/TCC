def eh_quadrada(matriz):
    """ """
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i is not j:
                return False 
            return True