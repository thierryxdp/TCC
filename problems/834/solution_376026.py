def media_matriz(matriz):
    """ Dada uma matriz de inteiros, não vazia, retorna a média de todos os números da matriz
    	list -> float
    """
    media = 0
    total = 0
    
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            media = media + media[i][j]
            total = total + 1
    media = media/total
    
    return round(media,2)