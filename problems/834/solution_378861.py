def media_matriz(matriz):
    """
    
    """
    numerador=0
    divisor=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numerador+=matriz[i][j]
            divisor+=1
   	
    media=numerador/divisor
    return round(media,2)