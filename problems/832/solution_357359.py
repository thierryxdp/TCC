def eh_quadrada(matriz):
    
    if len(matriz) < 1:
        return True
    
    else:
        
        for indice in matriz:
            ind = int(indice)
            if len(matriz[ind]) == len(matriz):
                return True
            
            else:
                False