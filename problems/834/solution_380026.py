def media_matriz(media):
    
    matriz=0
    a = len(media)
    b = len(media[0])
    
    for i in range (a):
        for j in range(b):
            matriz = matriz + media[i][j]
            
     

    final = matriz/(a)*(b)
            
    return round(final,2)