def eh_quadrada(matriz):
    
    if len(matriz) < 1:
        return True
    
    else:
        
        for indice in matriz:
            if len(matriz[indice]) == len(matriz):
                return True
            
            else:
                False