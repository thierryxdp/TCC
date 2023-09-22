def media_matriz(m):
    '''
    	essa função recebe uma matriz e calcula a media de todos os numeros da matriz com
        exatas duas casas decimais de precisão
        list -> float
    '''
    nLinha= len(m)
    nColuna= len(m[0])
    media = 0
    for i in range(nLinha):
        for j in range(nColuna):
            media = media + m[i][j]
    media = media/(nLinha*nColuna)
    return round(media, 2)