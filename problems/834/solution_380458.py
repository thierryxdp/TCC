def media_matriz(matriz):
    '''
    Recebe uma matriz e retorna a média de todas as suas entradas
    
    list -> float
    '''
    i=0
    soma=0
    while i<len(matriz):
        j=0
        while j<len(matriz[i]):
            soma+=matriz[i][j]
            j+=1
    media=soma/(len(matriz)*len(matriz[0]))
    return round(media,2)