def media_matriz(m):
    '''Retorna a média dos elementos da matriz m de entrada;
       list -> float'''
    nLin=len(m)
    nCol=len(m[0])
    soma=0
    for i in range(nLin):
        for j in range(nCol):
            soma+=m[i][j]
    media=soma/(nLin*nCol)
    return round(media,2)