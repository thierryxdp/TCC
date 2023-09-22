def media_matriz(matriz):
    '''docs'''
    
    somatorio = 0
    
    for i in range(len(matriz)):
        somatorio += sum(matriz[i])
        
    return somatorio