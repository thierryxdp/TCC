def media_matriz(m):
    '''
    retorna a media com duas casas decimais de todo os elementos da matriz m
    int -> float
    '''
    media=[]
    nlin = len(m)
    ncol = len(m[0])
    qtd_elem = 0
    for i in range(nlin):
        for el in range(ncol):
            media.append(m[i][el])
            qtd_elem = qtd_elem + 1
    return qtd_elem