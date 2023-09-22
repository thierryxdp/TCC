def media_matriz(matriz):
    '''calcula média de todos os elementos de uma matriz
    e retorna resultado com duas casas de precisão. 
    list --> float'''
    soma = 0
    i = 0
    
    for item in matriz:
        for item_2 in item:
            soma += item_2
            i += 1		
    media = soma/ i
    return round(media,2)