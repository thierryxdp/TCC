def media_matriz(matriz):
    '''Essa função retorna a media de todos os numeros da matriz.
    list >>> float '''
    soma = 0
    i = 0
    
    for item in matriz:
        for item_2 in item:
            soma += item_2
        	i += 1
        
    media = soma/ i
    return round(media,2)