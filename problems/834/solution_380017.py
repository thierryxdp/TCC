def media_matriz(media):
    
    matriz=0
    
    total = (len(media)*(len(media[0]))
    a = len(media)
    b = len(media[0])
    
    
    for i in range (a):
        for j in range(b):
            matriz += media[i][j]

    final = matriz//total
            
    return round(final,2)