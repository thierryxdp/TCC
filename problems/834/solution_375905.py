def media_matriz(matriz):
    '''Função que retorna a média de todos os números da matriz;list->float'''
    contador=0
    for i in matriz:
        for j in i:
            contador=contador+j
    media=contador/(len(matriz) * len(matriz[0]))
    return round(media,2)