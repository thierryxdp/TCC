def media_matriz(matriz):
    """ """
    numeros = 0
    
    somatorio = 0
    media = 0
    
    for lin in range(0,len(matriz)):
        
        for coluna in range(0,len(matriz[lin])):
           
        	numeros += 1
            somatorio +=  matriz[lin][col]
            media = somatorio / numeros
            
    return round(media,2)