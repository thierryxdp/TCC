def media_matriz(media):
    
    matriz=0
    
    
    for i in range (len(media)):
        for j in range(len(media[0])):
            matriz += media[i][j]
            
     

    final = matriz/(len(media)*(len(media[0]))
            
    return round(final,2)