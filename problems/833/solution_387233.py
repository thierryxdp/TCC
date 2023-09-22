def conta_numero(numero, matriz):   
    
    final= 0
    
    if matriz== []:        
        return final
        
    for a in range(len(matriz)):
        for b in range(len(matriz[0])):
            
            if matriz[a][b]== numero:
                final+= 1
            
    return final