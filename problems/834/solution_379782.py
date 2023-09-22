def media_matriz(matriz):
    '''Funcao que dada uma matriz de inteiro não vazia, retorna
       a media de todos os numeros da matriz(com exatamente duas
       casas decimais de precisão.
       : param matriz: list
       : param soma: int
       : param media: float
    '''
    soma=0
    media=0
    nlin=len(matriz)
    ncol=len(matriz[0])
    for i in range(nlin):
        for j in range(ncol): 
             soma+=matriz[i][j]
    denominador=(nlin)*(ncol)
    media=soma/denominador
    return round(media,2)