def media_matriz(media):
    
    matriz=0
    
    total = (len(media)*(len(media[0]))
    
    
    for i in range(len(media)):
        for j in range(len(media[0])):
            matriz += media[i][j]

    final = matriz/total
            
    return round(final,2)