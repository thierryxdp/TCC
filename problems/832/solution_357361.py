def eh_quadrada(matriz):
    
    if len(matriz) < 1:
        return True
    
    else:
        
        for indice in range(len(matriz)):
            if len(matriz[indice]) == len(matriz):
                return True
            
            else:
                return False