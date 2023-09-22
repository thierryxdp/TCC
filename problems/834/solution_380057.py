def media_matriz(matriz):
    '''docs'''
    
    somatorio = 0
    
    for i in range(len(matriz)):
        
        for j in range(len(matriz)):
            somatorio += matriz[i][j]
            
    return somatorio / (i + j)