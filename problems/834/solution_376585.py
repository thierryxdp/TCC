def media_matriz(matriz):
    
    acumulador = 0
    media = 0
    
    if matriz != []:
        m = len(matriz)
        n = len(matriz[0])
        
        for i in range(m):
            for j in range(n):
                acumulador += matriz[i][j]
        
        media = acumulador/(m*n)
    
    return round(media, 2)