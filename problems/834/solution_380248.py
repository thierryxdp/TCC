def media_matriz(matriz):
    '''Essa função retorna a media de todos os numeros da matriz.
    list >>> float '''
    soma = 1
    i = 1
    
    for item in matriz:
        for item_2 in item:
            soma += item_2
        	i += 1
        
    media = soma/ i
    return round(media,2)