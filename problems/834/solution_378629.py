def media_matriz (m):
    '''calcula e retorna a media dos numeros da matriz de entrada'''
    '''list-> float'''
    final = []
    for numero in m:
        for i in numero:
            final+=[i,]
     
    media = round(sum(final)/len(final),2)
    return media