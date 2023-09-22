def media_matriz(matriz):
    '''docs'''
    
    somatorio = 0
    elementos = 0
    for i in range(len(matriz)):
        somatorio += sum(matriz[i])
        elementos += len(matriz[i])
        media = round(somatorio / elementos, 2)
    return media