def media_matriz(matriz):
    '''calcula média de todos os elementos de uma matriz
    e retorna resultado com duas casas de precisão
    list--> float'''

    soma = 0  #inicia contador em zero
    contador = 0  #inicia contador em zero
    
    for item in matriz:  #para cada item da matriz:
        for item2 in item:  #para cada item dos itens da matriz:
            soma += item2  #soma item
            contador += 1  #incrementa contador

    media = soma/contador  #calcula média da soma dos itens
    
    return round(media, 2)  #retorna media com duas casas de precisão