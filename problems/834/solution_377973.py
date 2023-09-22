def media_matriz(matriz):
    '''Função que retorna a média dos números da matriz
    		list -> int '''
    media=0
    for l in matriz:
        for num in l:
            media += num
    return round(media/(len(matriz)*len(matriz[0])),2)