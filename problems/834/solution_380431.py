def media_matriz(matriz):
    '''calcula m ́edia de todos os elementos de uma matriz
e retorna resultado com duas casas de precis~ao
list--> float'''
    soma = 0 
    contador = 0 
    for i in matriz:
        for j in i:
            soma += j
            contador += 1
            media = soma/contador
    return round(media, 2)