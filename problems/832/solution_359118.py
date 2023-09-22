def eh_quadrada(matriz):
    """ """
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                return 'true' 
    return 'false'