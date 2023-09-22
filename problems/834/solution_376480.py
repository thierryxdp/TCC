def media_matriz(matriz):
    n = 0
    d = len(matriz[0])*len(matriz)
    
    for i in range(len(matriz)):
        n = n+sum(matriz[i])
            
    return round(n/d,2)