def media_matriz(media):
    
    
    for i in range(len(media)):
        for j in range(len(media[0])):
            soma += media[i][j]

    final = soma/total_termos
            
    return round(final,2)