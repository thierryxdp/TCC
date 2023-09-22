def media_matriz(x):
    '''
    funcao retorna a media da matriz, somando e fazendo a media de cada matriz e repetindo o mesmo com os resultados
    '''
    som=0
    tam=0
    for l in x:
        som+=sum(l)
        tam+=len(l)
    return round(som/tam,2)