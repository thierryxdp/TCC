def media_matriz(matriz):
    '''
    Função que dada uma matriz de unteiros nao vazia, 
    retorna a media de todos os numeros da matriz
    list -> float
    '''
    i = 0
    for linha in matriz:
        for elemento in linha:
            i = i + elemento
        media = i/(len(matriz)*len(matriz[0]))
    return round(media,2)