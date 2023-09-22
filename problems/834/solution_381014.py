def media_matriz(m):
    '''funçao que dada uma matriz de inteiros nao fazia,retorna a media
    de todos os numeros da matriz; list ->int'''
    x = 0
    for a in range (len(m)):
        for b in range(len(m[i])):
            x=x+m[a][b]
    media= x/(len(m)*len(m[0]))
    return round(media,2)