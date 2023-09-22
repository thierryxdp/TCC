def media_matriz(media):
    
    matriz=0
    
    
    for i in range (len(media)):
        for j in range(len(media[0])):
            matriz += media[i][j]
            
    total = (len(media)*(len(media[0]))

    final = matriz/total
            
    return round(final,2)