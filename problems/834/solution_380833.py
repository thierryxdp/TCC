def media(m):
    '''calcula e retorna a media de todos os numeros de uma matriz
    list -> float'''
    soma=0
    numeros=0
    nlin=len(m)
    ncol=len(m[0])
    for i in range(nlin):
        for j in range(ncol):
            soma=soma+m[i][j]
            numeros=numeros+1
    media=soma/numeros
    return round(media,2)