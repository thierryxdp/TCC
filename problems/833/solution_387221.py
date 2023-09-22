def conta_numero(numero, matriz):
    
    
    final = 0
    
    
    if matriz == []:        
        return final
        

    for i in range(len(matriz)):
        
        for j in range(len(matriz[0])):
            
            if matriz[i][j] == numero:
                final = final + 1
            
    return final